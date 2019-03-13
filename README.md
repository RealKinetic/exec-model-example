Exec model example for Kubernetes
=================================

This repo provides a demonstration of an operator pod execing into a list of
workload pods all running in the same namespace.

The ``/runme.sh`` is called in non-interactive mode in the workload pod from
the operator pod using the kubernetes api.

Running the demo
----------------

Install/run [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/). I am using kubernetes v1.13.2.
Install [skaffold](https://skaffold.dev/). I am using version v0.24.0

In the root folder of this repo, run ``skaffold dev``.

After the containers are built locally, you should see output similar to the following:

```bash
[operator-74f58497f8-84wqr exec-operator] starting loop ..
[operator-74f58497f8-84wqr exec-operator] Execing into workload-9bc876ddf-ws6c5 ..
[operator-74f58497f8-84wqr exec-operator] workload-9bc876ddf-ws6c5: like a baws!
[operator-74f58497f8-84wqr exec-operator]
[operator-74f58497f8-84wqr exec-operator] finished loop.
```
