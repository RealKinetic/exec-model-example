import time

from kubernetes import client, config
from kubernetes.stream import stream
from kubernetes.client.rest import ApiException


def list_workload_pods(api):
    ret = api.list_namespaced_pod(
        "juju",
        label_selector="app=workload",
        watch=False
    )

    for i in ret.items:
        yield i.metadata.name, i


if __name__ == "__main__":
    config.load_incluster_config()

    api = client.CoreV1Api()

    while True:
        print("starting loop ..")

        for name, pod in list_workload_pods(api):
            if pod.status.phase != 'Running':
                print("Skipping non running pod %s" % (name,))

                continue

            print("Execing into %s .." % (name,))

            try:
                response = stream(api.connect_get_namespaced_pod_exec,
                    name,
                    "juju",
                    command=["/bin/sh", "-c", "/runme.sh"],
                    stderr=True,
                    stdin=False,
                    stdout=True,
                    tty=False,
                )
            except ApiException as err:
                print("Failed to connect to pod.")

                continue

            print("%s: %s" % (name, response))

        print("finished loop.", flush=True)

        time.sleep(5.0)
