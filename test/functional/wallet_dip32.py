#!/usr/bin/env python3
# Copyright (c) 2019-2020 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Test descriptor wallet function."""

from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import (
    assert_equal,
    assert_not_equal,
    assert_raises_rpc_error
)

class WalletDIP32Test(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = True
        self.num_nodes = 1

    def skip_test_if_missing_module(self):
        self.skip_if_no_wallet()

    def run_test(self):
        # Check that getnewaddress works
        self.log.info("Test that getnewctaddress works")
        addr = self.nodes[0].getnewctaddress()

        assert_not_equal(addr, "")

if __name__ == '__main__':
    WalletDIP32Test().main ()
