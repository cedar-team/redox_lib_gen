# -*- coding: utf-8 -*-
import re

from snapshottest.pytest import PyTestSnapshotTest


class NoSpacesPyTestSnapshotTest(PyTestSnapshotTest):
    # Need to override a couple things from snapshottest so that filenames don't have
    # spaces (which causes black to choke in CI).
    @property
    def test_name(self):
        cls_name = getattr(self.request.node.cls, "__name__", "")
        flattened_node_name = re.sub(
            r"\s+", " ", self.request.node.name.replace(r"\n", " ")
        )
        return (
            f'{f"{cls_name}." if cls_name else ""}'
            f"{flattened_node_name}_{self.curr_snapshot}"
        )
