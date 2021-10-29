"""

"""


class JobNode:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.no_of_prereq = 0


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}

        for job in jobs:
            self.addNode(job)

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)

        return self.graph[job]

    def addDep(self, job, dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.deps.append(depNode)
        depNode.no_of_prereq += 1

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.addDep(job, dep)
    return graph


def topological_sort(job, deps):
    job_grap = createJobGraph(job, deps)
    return get_ordered_jobs(job_grap)


def get_ordered_jobs(graph):
    ordered_job = []
    node_with_no_prereq = list(filter(lambda node: node.no_of_prereq == 0, graph.nodes))

    while len(node_with_no_prereq):
        node = node_with_no_prereq.pop()
        ordered_job.append(node.job)
        remove_dependency(node, node_with_no_prereq)
    graph_has_edges = any(node.no_of_prereq for node in graph.nodes)
    return [] if graph_has_edges else ordered_job


def remove_dependency(node, node_with_no_prereq):
    while len(node.deps):
        dep = node.deps.pop()
        dep.no_of_prereq -= 1
        if dep.no_of_prereq == 0:
            node_with_no_prereq.append(dep)


if __name__ == "__main__":
    print(topological_sort([1, 2, 3, 4], [(1, 2), (1, 3), (3, 2), (4, 2), (4, 3)]))
