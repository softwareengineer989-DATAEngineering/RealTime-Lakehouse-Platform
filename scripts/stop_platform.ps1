Write-Host ""
Write-Host "==============================================="
Write-Host " RealTime Lakehouse Platform Shutdown"
Write-Host "==============================================="
Write-Host ""

Write-Host "[1/3] Stopping Bronze Streaming Pipeline..."

docker exec retail-spark pkill -f "retaillake.spark.streaming.bronze_stream"

Start-Sleep -Seconds 2

Write-Host ""
Write-Host "[2/3] Stopping Silver Streaming Pipeline..."

docker exec retail-spark pkill -f "retaillake.spark.silver.run_silver_stream"

Start-Sleep -Seconds 2

Write-Host ""
Write-Host "[3/3] Stopping Gold Streaming Pipeline..."

docker exec retail-spark pkill -f "retaillake.spark.gold.run_gold_stream"

Start-Sleep -Seconds 2

Write-Host ""
Write-Host "Verifying streaming services..."

Write-Host ""

docker exec retail-spark ps -ef | Select-String bronze

docker exec retail-spark ps -ef | Select-String silver

docker exec retail-spark ps -ef | Select-String gold

Write-Host ""

Write-Host "===================================================="
Write-Host "Platform shutdown completed successfully."
Write-Host "===================================================="

Write-Host ""

Write-Host "If you also want to stop Docker containers, run:"

Write-Host ""

Write-Host "docker compose down"

Write-Host ""

Write-Host "===================================================="