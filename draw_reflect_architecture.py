# diagram.py
from ntpath import join
from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.programming.framework import React
from diagrams.programming.language import Python, Rust
from scour import scour

filename = "website/reflect_architecture"
outformat = "svg"
full_filename = f"{filename}.{outformat}"

graph_attr = {
    "fontsize": "30",
    "pad": "0",
    "nodesep": "0",
    "ranksep": "1.5",
}
node_attr = {"fontsize": "15"}
cluster_attr = {"fontsize": "15", "margin": "0"}

KERNEL_APPS = [
    ["b", "e"],
    [
        "a",
        "d",
        "c",
    ],
    ["f"]
]

with Diagram(
    filename=filename,
    show=False,
    outformat="svg",
    graph_attr=graph_attr,
    node_attr=node_attr,
):
    with Cluster(
        "Server",
        graph_attr={
            "fontsize": "15",
        }, direction="LR",
    ):
        with Cluster("") as server:
            server = Rust("App server", height="1.6", imagepos="tc")
        for e, apps in zip(reversed(range(1, len(KERNEL_APPS) + 1)), KERNEL_APPS):
            with Cluster(f"Kernel {e}", graph_attr=cluster_attr, direction="TB"):
                (
                    server
                    << Edge()
                    >> Python(
                        "runs: " + ", ".join(str(i) for i in apps),
                        height="1.6",
                        imagepos="tc",
                        ranksep="0",
                        fontsize="15",
                    )
                )
    for i, apps in [(1, ["a", "b", "f"]), (2, ["c"]), (3, ["d", "e"])]:
        with Cluster(f"User machine {i}", graph_attr={"fontsize": "15"}):
                (
                    React(
                        f"apps: " + ", ".join(str(j) for j in apps),
                        fontsize="15",
                        height="1.6",
                        imagepos="tc",
                    )
                    << Edge()
                    >> server
                )

out_string = scour.scourString(open(full_filename, "r").read())
open(full_filename, "w").write(out_string)
