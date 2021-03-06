import argparse

from save_results import save_results_epi


def run_save_results(me_id, year_id, measure_id, description, input_dir):
    save_results_epi(input_dir=input_dir,
                     input_file_pattern="{location_id}.csv",
                     modelable_entity_id=me_id,
                     description=description,
                     year_id=year_id,
                     measure_id=measure_id,
                     gbd_round_id=5,
                     mark_best=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--me_id",
            help="me_id to upload to",
            type=int)
    parser.add_argument(
            "--year_id",
            help="year_id(s) in data",
            type=str)
    parser.add_argument(
            "--measure_id",
            help="measure_id in data",
            type=int)
    parser.add_argument(
            "--description",
            help="description of estimates",
            type=str)
    parser.add_argument(
            "--input_dir",
            help="directory where files are saved",
            type=str)
    args = parser.parse_args()
    me_id = args.me_id
    year_id = [int(i) for i in args.year_id.split()]
    measure_id = args.measure_id
    description = args.description
    input_dir = args.input_dir
    run_save_results(me_id, year_id, measure_id, description, input_dir)
