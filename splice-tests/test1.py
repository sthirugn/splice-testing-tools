import splicetestlib
from splicetestlib.splice_testcase import *
import datetime
import nose

class test_splice_1(SpliceTestcase, Splice_has_FAKE_SPACEWALK, Splice_has_Manifest):
    def _setup(self):
        splicetestlib.fake_spacewalk_env(self.ss.Instances["FAKE_SPACEWALK"][0], "test1")
        splicetestlib.sst_step(self.ss.Instances["FAKE_SPACEWALK"][0])
        # uploading manifest
        self.katello.upload_manifest("2", self.ss.config["manifest"])
        for step in range(36):
            splicetestlib.sst_step(self.ss.Instances["FAKE_SPACEWALK"][0])

    def test_01_active_week(self):
        """
        Active report last week
        Expecting 1 current and 1 invalid subscription
        """
        self.splice_check_report(days_start=7, days_end=1, current=1, invalid=1)

    def test_02_inactive_week(self):
        """
        Inactive report last week
        Expecting 0 subscriptions
        """
        self.splice_check_report(days_start=7, days_end=1, inactive=True)

    def test_03_active_next_week(self):
        """
        Active report next week
        Expecting 0 subscriptions
        """
        self.splice_check_report(days_start=-1, days_end=-7)

    def test_04_inactive_next_week(self):
        """
        Inactive report next week
        Expecting 1 current and 1 invalid subscription
        """
        self.splice_check_report(days_start=-1, days_end=-7, inactive=True, current=1, invalid=1)

    def test_05_active_past_24h(self):
        """
        Active report last 24h
        Expecting 1 current and 1 invalid subscription
        """
        self.splice_check_report(past_hours=24, current=1, invalid=1)

    def test_06_inactive_past_24h(self):
        """
        Inactive report last 24h
        Expecting 0 subscriptions
        """
        self.splice_check_report(past_hours=24, inactive=True)

    def _cleanup(self):
        splicetestlib.cleanup_katello(self.ss.Instances["KATELLO"][0])

if __name__ == "__main__":
    nose.run(defaultTest=__name__, argv=[__file__, '-v'])
