import re

pattern = r'ab*'

text = 'abc abbc abbcc abbbc'

# match() : 문자열의 처음부터 정규식과 매치되는지 조사한다.
match_result = re.match(pattern, text)
print("=== match() ===")
if match_result:
    print("Match found:", match_result.group())
else:
    print("No match found")
print("================")

# search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
search_result = re.search(pattern, text)
print("=== search() ===")
if search_result:
    print("Match found:", search_result.group())
else:
    print("No match found")
print("================")

# findall()  : 정규식과 매치되는 모든 문자열을 리스트로 리턴
findall_result = re.findall(pattern, text)
print("=== findall() ===")
if findall_result:
    print("Matches found:", findall_result)
else:
    print("No matches found")
print("================")

# finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴
finditer_result = re.finditer(pattern, text)
print("=== finditer() ===")
for match in finditer_result:
    print("Match found:", match.group())
print("================")

# match 객체의 매서드
# group() : 매치된 문자열을 리턴
# start() : 매치된 문자열의 시작위치 리턴
# end() : 매치된 문자열의 끝 위치를 리턴
# span() : 매치된 문자열의 (시작,끝)에 해당하는 튜플을 리턴

print("=== match 객체의 매서드 ===")
match_result = re.search(pattern, text)

if match_result:
    matched_text = match_result.group() 
    start_pos = match_result.start()     
    end_pos = match_result.end()         
    match_span = match_result.span()    

    # Print the match information
    print("=== Match Details ===")
    print("Matched Text:", matched_text)
    print("Start Position:", start_pos)
    print("End Position:", end_pos)
    print("Match Span:", match_span)
else:
    print("No match found")
print("================")

