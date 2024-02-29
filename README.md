## Bench CLI Demo

This app demonstrates how to create custom commands in Bench.

## Install the App

1. Create the Frappe site with [Frappe Manager (FM)](https://github.com/rtCamp/Frappe-Manager/):

```bash
fm create bench-cli-demo --frappe-branch version-15 --apps erpnext:version-15 --apps hrms:version-15
```

2. Install the app on your site:

```bash
fm shell bench-cli-demo
bench get-app https://github.com/zeel-codder/bench-cli-demo.git
bench --site {site-name} install-app bench_cli_demo
```

3. Test Commands:

```bash
bench sum 20 2
bench insert-todo
```

Note: You can set the default site with the following command:

```bash
bench use bench-cli-demo.localhost
```

## Setup the App for Importing Job Applicant Data

1. Download any CSV data from [here](https://drive.google.com/drive/folders/1eYJ6KXJf_3m3usGwYXb9_4wal7RCZr3x?usp=sharing) and move the file to the `frappe-bench` folder.

2. Define the file path in `common_site_config.json`:

```json
    "importer_csv_paths":{
        "job_applicant_data":"/workspace/frappe-bench/job_applicant_data_20K.csv"
    }
```

3. Run the import command:

```bash
bench rt-import import-job-applicant
```

## License

MIT
