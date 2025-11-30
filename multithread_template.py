# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm
import threading
import argparse
import requests
import json
import time
import os

from util import time

BATCH_SIZE = 10000
MAX_THREADS = 20
TIMEOUT_SECONDS = 20

SELECTED_ENVIRONMENT = None

session = requests.Session()

retries = Retry(
    total=1,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET", "POST", "PUT", "DELETE" "PATCH"],
)

adapter = HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)


def http_request(
    method: str,
    ip: str,
    port: int,
    url: str,
    opr: str,
    calls: list,
    https: bool = False,
    headers: dict = None,
    payload: dict = None,
    data_response: bool = False,
    raise_exception: bool = True,
):
    scheme = "https" if https else "http"
    full_url = f"{scheme}://{ip}:{port}{url}"
    response = session.request(
        method=method,
        url=full_url,
        headers=headers or {},
        json=payload if payload else None,
        timeout=TIMEOUT_SECONDS,
        verify=False,
    )
    data = response.text
    calls.append(
        f"INFO: {time.get_current_datetime()} | {url} | {method} | HTTP {response.status_code}\n"
        f"{json.dumps(payload,indent=4) if payload else 'Sem payload'}"
        f"\n{data if not str(response.status_code).startswith('2') else 'Sucesso na operacao'}",
    )
    if response.ok:
        return response.json() if data_response else True
    elif raise_exception:
        raise Exception(
            f"Error: {opr} | code: {response.status_code} | mensage: {data}"
        )
    return response.json() if data_response else False


def engine(**kwargs):
    try:
        calls = []
        status = None
        data = kwargs["data"].split(",")
        status = "OK"
    except Exception as e:
        status = str(e)
    finally:
        with lock:
            pass


def write_log(message: str, filename: str):
    with open(f"{filename}.txt", "a", encoding="utf8") as log:
        log.write(message + "\n")


def count_lines(file):
    counter = 0
    with open(file, "r") as csv:
        for _ in csv:
            counter += 1
    return counter


def run_threads(executor, batch, file, pbar):
    futures = [executor.submit(engine, data=l, identifier=file) for l in batch]
    [pbar.update(1) for _ in as_completed(futures)]
    batch.clear()


def runner():
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        batch = []
        with tqdm(total=count_lines(args.file), desc=args.file, unit="linha") as pbar:
            with open(args.file, "r") as csv:
                for line in csv:
                    batch.append(line)
                    if len(batch) >= BATCH_SIZE:  # avoid thread overhead
                        run_threads(executor, batch, args.file, pbar)
                run_threads(executor, batch, args.file, pbar)
        print(f"===== Fim {args.file} ======")


if __name__ == "__main__":
    start_time = time.time()
    start_time_datetime = time.get_current_datetime()
    parser = argparse.ArgumentParser(description="<DESCRIÇÃO SCRIPT")
    parser.add_argument(
        "-f",
        "--file",
        help="arquivo que será executado",
        dest="file",
        type=str,
        action="store",
        required=True,
    )
    args = parser.parse_args()
    IDENTIFIER = args.file.split("_")[1].replace(".txt", "")
    os.makedirs(f"exec_{IDENTIFIER}")
    lock = threading.Lock()
    runner()
    os.replace(args.file, f"exec_{IDENTIFIER}/{args.file}")
    delta_hora = f"{(int(time.time() - start_time))/3600:.2f}"
    delta_minuto = f"{(int(time.time() - start_time))/60:.2f}"
    total = int(os.popen(f"cat exec_{IDENTIFIER}/status_*.txt | wc -l").read().strip())
    sucesso = int(
        os.popen(f"cat exec_{IDENTIFIER}/status_OK.txt | wc -l").read().strip()
    )
    falha = int(
        os.popen(f"cat exec_{IDENTIFIER}/status_NOK.txt | wc -l").read().strip()
    )
    report = {
        "tag": "<TAG>",
        "horaInicio": start_time_datetime,
        "horaFim": time.get_current_datetime(),
        "deltaHora": delta_hora,
        "deltaMinuto": delta_minuto,
        "total": total,
        "sucesso": sucesso,
        "falha": falha,
        "aproveitamento": f"{sucesso * 100 / total:.2f}%" if total > 0 else "0%",
        "file": f"exec_{IDENTIFIER}/{args.file}",
    }
    write_log(json.dumps(report, indent=4), "exec_info")
