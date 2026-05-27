#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""
import os
import argparse

from inflammation import models, views, analysis


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = args.infiles
    if not isinstance(in_files, list):
        in_files = [args.infiles]

    for filename in in_files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            "average": models.daily_mean(inflammation_data),
            "max": models.daily_max(inflammation_data),
            "min": models.daily_min(inflammation_data),
        }

        views.visualize(view_data)

    data_dir =os.path.dirname(in_files[0])
    # construct an appropriate data source instance based on the file extension

    if in_files[0].endswith('.csv'):    
        data_source = analysis.CSVDataSource(data_dir)
    elif in_files[0].endswith('.json'):
        data_source = analysis.JSONDataSource(data_dir)
    else:
        raise ValueError(f"Unsupported file format for {in_files[0]}")

    data = data_source.load_inflammation_data()
    print("Loaded data:", data.head())





if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A basic patient inflammation data management system"
    )

    parser.add_argument(
        "infiles",
        nargs="+",
        help="Input CSV(s) containing inflammation series for each patient",
    )

    args = parser.parse_args()

    main(args)
