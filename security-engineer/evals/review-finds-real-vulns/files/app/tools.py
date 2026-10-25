import subprocess


def archive_logs(date):
    # date is validated upstream as YYYY-MM-DD
    subprocess.run(["tar", "czf", f"logs-{date}.tgz", "logs/"], check=True)
