"""
Enterprise Validation Report Writer

Generates

- platform_validation_report.json
- platform_validation_report.html

Enterprise evidence report for validation framework.
"""

from __future__ import annotations

import html
import json

from datetime import datetime
from pathlib import Path

from retaillake.validation.validation_result import ValidationResult


def _format_metric(key: str, value) -> str:
    """
    Converts metrics into readable HTML.

    Special handling is applied for Spark schema
    strings so they are displayed as formatted
    multi-line metadata instead of a single long line.
    """

    if isinstance(value, bool):
        return "Yes" if value else "No"

    if isinstance(value, float):
        return f"{value:.3f}"

    if isinstance(value, (list, tuple)):
        if not value:
            return "-"

        return ", ".join(map(str, value))

    if value is None:
        return "-"

    if (
        key.lower() == "schema"
        and isinstance(value, str)
    ):
        formatted = (
            value
            .replace("struct<", "")
            .replace(">", "")
            .replace(",", "\n")
            .replace(":", " : ")
        )

        return (
            "<pre class=\"schema-block\">"
            f"{html.escape(formatted)}"
            "</pre>"
        )

    return html.escape(str(value))


def _build_metrics_table(metrics: dict) -> str:
    """
    Render validator metrics.
    """

    if not metrics:
        return "<em>No metrics collected.</em>"

    rows = []

    for key, value in metrics.items():

        rows.append(
            f"""
<tr>
<td class="metric-name">
{html.escape(str(key))}
</td>

<td>
{_format_metric(key, value)}
</td>

</tr>
"""
        )

    return f"""
<table class="metrics-table">

<thead>

<tr>

<th>Metric</th>

<th>Value</th>

</tr>

</thead>

<tbody>

{''.join(rows)}

</tbody>

</table>
"""

def write_report(
    results: list[ValidationResult],
    report_directory: Path,
) -> dict[str, Path]:
    """
    Generate enterprise validation reports.

    Returns
    -------
    {
        "json": Path(...),
        "html": Path(...)
    }
    """

    report_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    json_report = (
        report_directory
        / "platform_validation_report.json"
    )

    html_report = (
        report_directory
        / "platform_validation_report.html"
    )

    generated_at = datetime.now().isoformat()

    total = len(results)

    passed = sum(r.passed for r in results)

    failed = total - passed

    report_data = {
        "generated_at": generated_at,
        "total_validators": total,
        "passed": passed,
        "failed": failed,
        "results": [],
    }

    validator_cards = []

    for result in results:

        report_data["results"].append(
            {
                "component": result.component,
                "passed": result.passed,
                "message": result.message,
                "metrics": result.metrics,
                "timestamp": result.timestamp.isoformat(),
            }
        )

        duration = result.metrics.get(
            "execution_time_seconds",
            0,
        )

        status = "PASS" if result.passed else "FAIL"

        card_class = (
            "validator-pass"
            if result.passed
            else "validator-fail"
        )

        validator_cards.append(
            f"""
<div class="validator-card {card_class}">

<div class="validator-header">

<div>

<h2>{html.escape(result.component)}</h2>

<div class="status">{status}</div>

</div>

<div class="duration">
{duration:.3f} sec
</div>

</div>

<p class="message">
{html.escape(result.message)}
</p>

{_build_metrics_table(result.metrics)}

</div>
"""
        )

    json_report.write_text(
        json.dumps(
            report_data,
            indent=4,
        ),
        encoding="utf-8",
    )

    html_document = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="utf-8">

<title>Platform Validation Report</title>

<style>

*{{
    box-sizing:border-box;
}}

body{{
    margin:0;
    padding:40px;
    background:#f4f6f9;
    color:#222;
    font-family:Segoe UI,Arial,sans-serif;
}}

.container{{
    max-width:1500px;
    margin:auto;
}}

h1{{
    color:#1f2937;
    margin-bottom:10px;
}}

.subtitle{{
    color:#666;
    margin-bottom:35px;
}}

.summary{{
    display:flex;
    gap:20px;
    flex-wrap:wrap;
    margin-bottom:35px;
}}

.summary-card{{
    background:white;
    border-radius:10px;
    padding:20px;
    min-width:220px;
    box-shadow:0 2px 8px rgba(0,0,0,.10);
}}

.summary-title{{
    font-size:14px;
    color:#666;
}}

.summary-value{{
    font-size:34px;
    font-weight:bold;
    margin-top:8px;
}}

.pass{{
    color:#15803d;
}}

.fail{{
    color:#dc2626;
}}

.validator-card{{
    background:white;
    border-radius:10px;
    padding:20px;
    margin-bottom:28px;
    box-shadow:0 2px 10px rgba(0,0,0,.12);
}}

.validator-pass{{
    border-left:7px solid #16a34a;
}}

.validator-fail{{
    border-left:7px solid #dc2626;
}}

.validator-header{{
    display:flex;
    justify-content:space-between;
    align-items:center;
}}

.status{{
    font-size:15px;
    font-weight:bold;
}}

.duration{{
    font-size:15px;
    color:#666;
}}

.message{{
    margin:18px 0;
}}

.metrics-table{{
    width:100%;
    border-collapse:collapse;
    table-layout:fixed;
    margin-top:15px;
}}

.metrics-table th{{
    background:#1f2937;
    color:white;
    padding:10px;
    text-align:left;
}}

.metrics-table td{{
    border:1px solid #ddd;
    padding:10px;
    vertical-align:top;
    white-space:normal;
    word-break:break-word;
    overflow-wrap:anywhere;
}}

.metric-name{{
    width:22%;
    font-weight:bold;
    background:#f9fafb;
}}

.metrics-table td:last-child{{
    width:78%;
}}

.schema-block{{
    margin:0;
    padding:10px;
    background:#f8fafc;
    border-radius:6px;
    white-space:pre-wrap;
    word-break:break-word;
    overflow-wrap:anywhere;
    font-family:Consolas,Monaco,monospace;
    font-size:13px;
    line-height:1.5;
}}

</style>

</head>

<body>

<div class="container">

<h1>Platform Validation Report</h1>

<p class="subtitle">

Enterprise Platform Validation Framework

</p>

<div class="summary">

<div class="summary-card">

<div class="summary-title">

Generated

</div>

<div class="summary-value" style="font-size:18px">

{generated_at}

</div>

</div>

<div class="summary-card">

<div class="summary-title">

Total Validators

</div>

<div class="summary-value">

{total}

</div>

</div>

<div class="summary-card">

<div class="summary-title">

Passed

</div>

<div class="summary-value pass">

{passed}

</div>

</div>

<div class="summary-card">

<div class="summary-title">

Failed

</div>

<div class="summary-value fail">

{failed}

</div>

</div>

</div>

<h2>Validator Results</h2>

{''.join(validator_cards)}

<hr style="margin-top:40px">

<p style="color:#666;font-size:13px;">

Generated automatically by the

<strong>RealTime-Lakehouse-Platform Validation Framework</strong>

</p>

</div>

</body>

</html>
"""

    html_report.write_text(
        html_document,
        encoding="utf-8",
    )

    return {
        "json": json_report,
        "html": html_report,
    }