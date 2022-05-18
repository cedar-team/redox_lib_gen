# -*- coding: utf-8 -*-
"""File snapshot test helpers.

This file is necessary because ``snapshottest``'s file snapshot tests with
``unittest`` result in snapshot files that have spaces in their names, which
Cedar's CI cannot handle. Directly monkey-patching the ``test_name`` resulted
in the tests passing for ``redox_lib_gen``, but caused all other snapshot tests
to fail in CI. So, this workaround allows for filenames that without spaces
without affecting the ``TestCase`` or ``UnitTestSnapshotTest`` classes used by
other Cedar tests.

For the record, ``snapshottest``'s set of ``pytest`` utilities do not have this
same problem.
"""

from snapshottest.diff import PrettyDiff
from snapshottest.module import SnapshotTest
from snapshottest.unittest import TestCase, UnitTestSnapshotTest


class FileSnapshotTest(UnitTestSnapshotTest):
    @property
    def test_name(self):
        test_name = self.test_id.split(".")[-1]
        return f"{test_name}_{self.curr_snapshot}"


class FileTestCase(TestCase):
    def setUp(self):
        self.addTypeEqualityFunc(PrettyDiff, self.comparePrettyDifs)
        self._snapshot = FileSnapshotTest(
            test_class=self.__class__,
            test_id=self.id(),
            test_filepath=self._snapshot_file,
            should_update=self.snapshot_should_update,
            assertEqual=self.assertEqual,
        )
        self._snapshot_tests.append(self._snapshot)
        SnapshotTest._current_tester = self._snapshot
