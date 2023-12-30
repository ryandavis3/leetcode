from typing import List
from unittest import TestCase


MOD = 10**9 + 7


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        pass


def get_num_music_playlists(n: int, goal: int, k: int) -> int:
    # Initialize a goal x n DP table.
    dp: List[List[int]] = []
    for _ in range(goal+1):
        dp += [[0] * (n + 1)]
    # One empty playlist
    dp[0][0] = 1
    # Iterate number of songs in playlist towards goal
    for i in range(1, goal+1):
        # Iterate number of unique songs
        for j in range(1, min(i, n) + 1):
            # The ith song is a new song
            dp[i][j] = dp[i-1][j-1] * (n - j + 1) % MOD
            # The ith song is a song we have played before
            if j > k:
                dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % MOD
    return dp[goal][n]


class TestMusicPlaylists(TestCase):
    def test1(self) -> None:
        num_playlists = get_num_music_playlists(n=3, goal=3, k=1)
        self.assertEqual(num_playlists, 6)

    def test2(self) -> None:
        num_playlists = get_num_music_playlists(n=2, goal=3, k=0)
        self.assertEqual(num_playlists, 6)

    def test3(self) -> None:
        num_playlists = get_num_music_playlists(n=2, goal=3, k=1)
        self.assertEqual(num_playlists, 2)