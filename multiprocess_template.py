from concurrent.futures import ProcessPoolExecutor, as_completed
import argparse
import os
import time
import json

MAX_PROCESSES = 4


def read_database_by_customer(identifier):
    try:
        start = time.time()
        status = "OK"
    except Exception as e:
        status = str(e)
    finally:
        end = time.time()
    return status, f"{(int(end - start))/60:.2f}", identifier


def write_log(message: str, filename: str):
    with open(f"{filename}.txt", "a") as log:
        log.write(message + "\n")


def run_engine(identifiers, log):
    with ProcessPoolExecutor(max_workers=MAX_PROCESSES) as executor:
        futures = [
            executor.submit(read_database_by_customer, identifier) for _ in identifiers
        ]
        for future in as_completed(futures):
            status, time, identifier = future.result()
            log[identifier] = {
                "status": status,
                "time": time,
                "identitifer": identifier,
            }
    return log


def main():
    partition_log = {identifier: None for identifier in args.partition}
    log = run_engine(args.partition, partition_log)
    identifier = get_current_datetime()
    return identifier, partition_log


if __name__ == "__main__":
    start_time_datetime = get_current_datetime()
    start_time = time.time()
    os.makedirs("temp")
    print(f"Main process pid: {os.getpid()}")
    parser = argparse.ArgumentParser(description="<Descrição script")
    parser.add_argument(
        "-i",
        "--identifier",
        help="Particao do banco que sera escaneada.",
        dest="partition",
        type=int,
        action="append",
        required=True,
    )
    args = parser.parse_args()
    identifier, partition_log = main()
    delta_hora = f"{(int(time.time() - start_time))/3600:.2f}"
    delta_minuto = f"{(int(time.time() - start_time))/60:.2f}"
    report = {
        "tag": "Extracao",
        "horaInicio": start_time_datetime,
        "horaFim": get_current_datetime(),
        "deltaHora": delta_hora,
        "deltaMinuto": delta_minuto,
        "partitionCheck": partition_log,
        "total": os.popen(f"cat input_{identifier}.txt | wc -l").read().strip(),
        "file": f"input_{identifier}",
    }
    write_log(json.dumps(report, indent=4), "bko_info")
