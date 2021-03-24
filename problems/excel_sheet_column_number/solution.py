class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_table = {}
        char_A = 'A'
        for num in range(0,26):
            column_table[chr(ord(char_A) + num)] = num + 1
        # print(column_table)
        
        power_list = [26**0, 26**1, 26**2, 26**3, 26**4, 26**5, 26**6, 26**7]
        # print(power_list)
        
        if len(columnTitle) > 1:
            columnTitle = columnTitle[::-1]
        idx = 0
        output = 0
        for column_char in columnTitle:
            output += column_table[column_char] * power_list[idx]
            idx += 1
        
        print(output)
        return output