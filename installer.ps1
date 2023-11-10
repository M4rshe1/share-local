# Define the Git repository URL and destination directory
$gitRepoURL = "https://github.com/M4rshe1/share-local/archive/refs/heads/main.zip"
$destinationDirectory = Get-Location

# Create a temporary ZIP file path
$tempZipFile = Join-Path $env:TEMP "share_local.zip"

# Download the Git repository as a ZIP file
Invoke-WebRequest -Uri $gitRepoURL -OutFile $tempZipFile

# Check if the download was successful
if (Test-Path $tempZipFile) {
    # Unzip the repository to the destination directory
    Expand-Archive -Path $tempZipFile -DestinationPath $destinationDirectory
    Write-Host "Git repository successfully downloaded and unzipped to $destinationDirectory"
} else {
    Write-Host "Failed to download the Git repository."
}
