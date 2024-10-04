class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n = len(skill)
        total_sum = sum(skill)

        target_sum = total_sum // (n // 2)
        chemistry_sum = 0
        for i in range(n // 2):
            team_sum = skill[i] + skill[n - 1 - i]

            if team_sum != target_sum:
                return -1
            chemistry_sum += skill[i] * skill[n - 1 - i]

        return chemistry_sum
