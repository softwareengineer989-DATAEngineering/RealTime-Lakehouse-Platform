Write-Host ""
Write-Host "==============================================="
Write-Host " RealTime Lakehouse Platform Startup"
Write-Host "==============================================="
Write-Host ""

Write-Host "[1/3] Starting Bronze Streaming Pipeline..."
docker exec -d retail-spark `
python3 -m retaillake.spark.streaming.bronze_stream

Start-Sleep -Seconds 8

Write-Host ""
Write-Host "[2/3] Starting Silver Streaming Pipeline..."
docker exec -d retail-spark `
python3 -m retaillake.spark.silver.run_silver_stream

Start-Sleep -Seconds 8

Write-Host ""
Write-Host "[3/3] Starting Gold Streaming Pipeline..."
docker exec -d retail-spark `
python3 -m retaillake.spark.gold.run_gold_stream

Start-Sleep -Seconds 5

Write-Host ""
Write-Host "===================================================="
Write-Host "Platform startup completed successfully."
Write-Host "===================================================="
Write-Host ""

Write-Host "Next Steps"
Write-Host "----------"
Write-Host ""

Write-Host "1. Run the Kafka producer to publish streaming events"
Write-Host ""
Write-Host "python src/retaillake/kafka/producer/stream_instacart.py"
Write-Host ""

Write-Host "2. Run the platform validation"
Write-Host ""
Write-Host "python scripts/validate_all.py"
Write-Host ""

Write-Host "3. Stop the platform when finished"
Write-Host ""
Write-Host ".\scripts\stop_platform.ps1"
Write-Host ""

Write-Host "===================================================="