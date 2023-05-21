# 정규표현식 
### ■ 정규표현식이 필요한 이유
정규 표현식이란?
- 복잡하고 특정한 규칙을 가진 문자열을 처리할 때 사용하는 기법
- 복잡한 문자열의 검색과 치환을 위해 사용됨
- 문자열을 처리하는 모든 곳에서 사용
- 정규표현식을 정규식이라고도 한다. 

### ■ 정규표현식이 필요한 이유
- 정규식을 사용하면 직관적인 코드를 작성할 수 있다.
- 간결한 코드 작성이 가능하다.

### ■ 정규표현식의 기초, 메타 문자
메타문자 : 원래 그 문자가 가진 뜻이 아닌 특별한 용로로 사용하는 문자<p>
  <pre><code> . ^ $ * + ? { } [ ] \ | ( ) </code></pre>  

### ■ 문자 클래스 [ ]
문자 클래스로 만들어진 정규식은 <code>"[]사이의 문자들과 매치"</code>라는 의미를 갖는다.<p>

>문자 클래스를 만드는 메타 문자인 [] 사이에는 어떤 문자도 들어갈 수 있음 <p>
  
#### 정규 표현식 [abc] -> 표현식의 의미 : "a,b,c 중 한개의 문자와 매치"
- "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
- "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
- "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음<p>
[] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(Form-To)를 의미<p>
정규표현식인 [a-c] = [a,b,c] , [0-5] = [012345]
- [a-zA-Z] : 알파벳 모두
- [0-9] : 숫자<p>
  문자클래스 안에는 어떤 문자나 메타 문자도 사용할 수 있다.<p>
  하지만, <code>^</code> 는 문자클래스에서 반대(not)의 의미를 갖는다.<p>
  ex) <code>[^0-9]</code>의 정규표현식은 숫자가 아닌 문자만 매치

### ■ Dot(.)
 Dot 메타문자는 줄바꿈 문자인 <code>\n</code>을 제외한 모든 문자와 매치됨을 의미
    
 <pre><code> a.b   #의미:"a+모든문자+"b"</code></pre> 
 a,b라는 문자 사이에 어떤 문자가 들어가도 모두 매치된다는 의미<p>
 문자열 "aab", "a0b", "abc"가 정규식 <code>a.b</code>와 어떻게 매치
  - "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 <code>.</code>과 일치하므로 정규식과 매치
 - "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 <code>.</code>과 일치하므로 정규식과 매치
 - "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않음
  
<pre><code> a[.]b   #의미:"a + Dot(.)문자 + b"</code></pre> 
따라서, 정규식 <code<a[.]b</code>는 "a.b" 문자열과 매치되고, "a0b" 문자열과는 매치되지 않는다<p>
  
### ■ 반복 (*)
<pre><code> ca*t</code></pre> 
정규식에는 반복을 의미하는 <code> * </code>메타 문자가 사용<p>
<code> * </code>는 앞의 있는 문자a가 0부터 문한대까지 반복될 수 있다는 의미<p>
※ 사실 메모리 제한으로 2억개 정도만 가능
  
|정규식|문자열|match 여부| 설명 |
|------|---|---|---|
|ca*t|ct|yes|"a"가 0번 반복되어 매치|
|ca*t|cat|yes|"a"가 0번 이상 반복되어 매치 (1번 반복)|
|ca*t|caaat|yes|"a"가 0번 이상 반복되어 매치 (3번 반복)|
 
### ■ 반복 (+)
<pre><code> ca+t #의미 : "c + a(1번 이상 반복) + t "</code></pre> 

|정규식|문자열|match 여부| 설명 |
|------|---|---|---|
|ca+t|ct|No|"a"가 0번 반복되어 매치되지 않음|
|ca+t|cat|yes|"a"가 1번 이상 반복되어 매치 (1번 반복)|
|ca+t|caaat|yes|"a"가 1번 이상 반복되어 매치 (3번 반복)|

### ■ 반복 ({m,n}, ?)
{}문자를 사용하면 반복횟수를 고정할 수 있다.<p>
{m,n} -> 횟수가 m부터 n까지 매치 할 수 있다. 
  - {3,} : 3이상
  - {,3} : 3이하
  > <code>{1,}</code> 은 <code> + </code>와 동일하고, <code>{0,}</code> 은 <code> * </code>와  동일
  #### 1. { m }  <p>
 <pre><code> ca{2}t #의미 : "c + a(반드시 2번 반복) + t"</code></pre> 
 
 |정규식|문자열|match 여부| 설명 |
|------|---|---|---|
|ca{2}t|cat|No|"a"가 1번만 반복되어 매치되지 않음|
|ca{2}t|caat|yes|"a"가 2번 반복되어 매치|

#### 2. { m,n }  <p>
 <pre><code> ca{2,5}t #의미 : "c + a(2~5회 반복) + t"</code></pre> 
 
 |정규식|문자열|match 여부| 설명 |
|------|---|---|---|
|ca{2,5}t|cat|No|"a"가 1번만 반복되어 매치되지 않음|
|ca{2,5}t|caat|yes|"a"가 2번 반복되어 매치|
|ca{2,5}t|caaaaat|yes|"a"가 5번 반복되어 매치|  

#### 3. ?  <p>
반복은 아니지만 이와 비슷한 개념으로 ?가 있다. <p>
<code>?</code>메타문자가 의미하는 것은 <code>{0,1}</code>
  
<pre><code> ab?c #의미 : "a + b(있어도 되고 없어도 된다) + c"</code></pre> 

|정규식|문자열|match 여부| 설명 |
|------|---|---|---|
|ab?c|abc|yes|"b"가 1번 사용되어 매치|
|ab?c|ac|yes|"b"가 0번 사용되어 매치|

즉 b문자가 있거나 없거나 둘 다 매치되는 경우<p>
*,+,? 메타문자는 모두 {m,n} 형태로 고쳐쓰는 것이 가능하지만 *,+,? 메타문자를 사용하는 것이 좋다.

### ■ 파이썬에서 정규 표현식을 지원하는 re 모듈
정규 표현식을 지원하기 위한 모듈
<pre><code>>> import re
>> p = re.compile('ab*') </code></pre> 
  
### ■ 정규식을 이용한 문자열 검색
|Method|목적|
|------|---|
|match()|문자열의 처음부터 정규식과 매치되는지 조사한다.|
|search()|문자열 전체를 검색하여 정규식과 매치되는지 조사한다.|
|findall()|정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.|
|finditer()|정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.|

#### match
<pre><code>>> m = p.match("python")
>> print(m) </code></pre> 
<re.Match object; span=(0, 6), match='python'>출력

<pre><code>>> m = p.match("3 python")
>> print(m) </code></pre> 
None 출력
-> 정규식 <code>[a-z]+</code>에 부합하지 않음

<pre><code>>> p = re.compile(정규표현식)
>> m = p.match('string goes here')
>> if m:
>>    print('Match found: ', m.group())
>> else:
>>    print('No match') </code></pre> 
match의 결과값이 있을 때만 그 작업을 수행하겠다는 것

#### search
<pre><code>>> m = p.search("python")
>> print(m) </code></pre> 
<re.Match object; span=(0, 6), match='python'>출력

<pre><code>>> m = p.search("3 python")
>> print(m) </code></pre> 
<re.Match object; span=(2, 8), match='python'> 출력<p>
-> 문자열 전체를 검색하기 때문에 python 문자열과 매치됨

#### findall
<pre><code>>> result = p.findall("life is too short")
>> print(result) </code></pre> 
['life', 'is', 'too', 'short'] 출력<p>
-> findall은 패턴([a-z]+)과 매치되는 모든 값을 찾아 리스트로 리턴

  
#### finditer
  <pre><code>>> result = p.finditer("life is too short")
>> print(result) </code></pre>
<callable_iterator object at 0x01F5E390>
<pre><code>>> for r in result: print(r) </code></pre>
... <p>
<re.Match object; span=(0, 4), match='life'> <p>
<re.Match object; span=(5, 7), match='is'><p>
<re.Match object; span=(8, 11), match='too'><p>
<re.Match object; span=(12, 17), match='short'><p>

### ■ match 객체의 매서드
|Method|목적|
|------|---|
|group()|매치된 문자열을 리턴한다.|
|start()|매치된 문자열의 시작 위치를 리턴한다.|
|end()|매치된 문자열의 끝 위치를 리턴한다.|
|span()|매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.|

<pre><code>>> m = p.match("python")
>> m.group() </code></pre>
'python'
<pre><code>>> m.start() </code></pre>
  0
<pre><code>>> m.end() </code></pre>
  6  
<pre><code>>> m.span() </code></pre>
(0, 6)  
