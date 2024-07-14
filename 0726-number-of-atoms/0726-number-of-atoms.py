class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        
        st = []
        i = 0
        n = len(formula)
        
        while i < n:
            
            char = formula[i]
            assci = ord(char)
            
            if char == "(":
                st.append(char)
                i += 1
            elif char == ")":
                value = 1
                i += 1
                
                j = i
                if i < n:
                    char = formula[i]
                    assci = ord(char)
                    while i < n and 48 <= assci <= 57:
                        i  += 1
                        if i >= n:
                            break
                        char = formula[i]
                        assci = ord(char)
                    
                if i-j >= 1:
                    value = int(formula[j:i])
                
                subans = {}
                elements = st.pop()
                while st and elements != "(":
                    for k, v in elements.items():
                        subans[k] = subans.get(k, 0) + v
                    elements = st.pop()
                
                if value > 1:
                    for k in subans:
                        subans[k] *= value
                
                st.append(subans)
                
            elif 65 <= assci <= 90:
                key = char
                value = 1
                
                i = i + 1
                if i < n:
                    char = formula[i]
                    assci = ord(char)
                    if 97 <= assci <= 122:
                        key += char
                        i += 1
                
                j = i
                if i < n:
                    char = formula[i]
                    assci = ord(char)
                    while i < n and 48 <= assci <= 57:
                        i  += 1
                        if i >= n:
                            break
                        char = formula[i]
                        assci = ord(char)
                    
                if i-j >= 1:
                    value = int(formula[j:i])
                
                st.append({key: value})
                continue
        
        ans  = {}

        while st:
            elements = st.pop()
            for k, v in elements.items():
                ans[k] = ans.get(k, 0) + v
        
        ans = sorted(ans.items())
        ansStr = ""
        for k, v in ans:
            if v == 1:
                ansStr += k
            else:
                ansStr += f'{k}{v}'
        
        return ansStr
                