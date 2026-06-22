# Valid Parenthesis String
# You are given a string s which contains only three types of characters: '(', ')' and '*'.

# Return true if s is valid, otherwise return false.

# - A string is valid if it follows all of the following rules:
# - Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Every right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
# **********************************************************
# *********** Using GREEDY [Very good][Use this] ***********
# **********************************************************


class Solution:
    def checkValidString(self, s: str) -> bool:
        # we need to have a range in which unmatched open bracket can lie
        open_range = [0, 0]  # righ now the no of unmatched open bracket lie in this range, ie - 0

        for ch in s:
            if ch == "(":  # increase the entire range to do +1
                open_range[0] += 1
                open_range[1] += 1
            elif ch == ")":  # decrease the entire range to do -1. one of the unmatched got matched
                open_range[0] -= 1
                open_range[1] -= 1
            else:  # in case of *, treat it as ( or ) or '' to winden the range, the star can be ( -> hence the range of unmatched b should increase
                open_range[0] -= 1  # reducing the min range as * can be )
                open_range[1] += 1  # increasing the max range as * can be (

                # star being '' is already handled as it doesn't change the range

            # at any given point, if the entire range went into -ve, that mean there are more closing bracked than opening,
            # this cannot be fixed as starts till this point is alreay accounted.
            if open_range[1] < 0:
                return False

            # ******* This is important and counter intuitive ******
            # s = (*)(
            # without this change we will return true instead of false for above string
            # this steps make sure that * caanot be assumed as ) -> this only lead it to go negative
            if open_range[0] < 0:
                open_range[0] = 0

        # At the end, the range should have 0 to be valid, think of it way, the possible range of unmatched paranthesis should have 0 as an option.
        # as 0 no of unmatched open bracked is needed for being valid
        return open_range[0] <= 0 <= open_range[1]
