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

<pre><code>>>  m = p.search("3 python")
>> m.group() </code></pre>
'python'
<pre><code>>> m.start() </code></pre>
  2
<pre><code>>> m.end() </code></pre>
  8  
<pre><code>>> m.span() </code></pre>
(2, 8)  
    
### ■ 컴파일 옵션
- DOTALL(S) - <code>.</code>이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 함
- IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 함.
- MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (<code>^</code>, <code>$</code> 메타문자의 사용과 관계가 있는 옵션이다)
- VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)<p>
-> 옵션을 사용할 때는 <code>re.DOTALL</code> 처럼 전체 옵션 이름 써도 되고 <code>re.S</code> 처럼 약어를 써도 됨
  
#### DOTALL, S
  <code>.</code>메타 문자는 줄바꿈 문자를 제외한 모든 문자와 매치되는 규칙이 있다.<p>
  줄바꿈 문자도 포함하여 매치하고 싶다면 <code>re.DOTALL</code> 또는 <code>re.S</code> 옵션을 사용해 정규식을 컴파일 하면 된다.
  <pre><code>>> import re
  >>> p = re.compile('a.b')
  >>> m = p.match('a\nb')
  >>> print(m) #None</code></pre>
정규식이 <code>a.b</code>인 경우 문자열 <code>a\nb</code>는 매치 되지 않는다.<p>
  그 이유는 <code>\n</code>은 <code>.</code>메타 문자와 매치되지 않기 때문이다.<p>

<pre><code>>> import re
  >>> p = re.compile('a.b', re.DOTALL)
  >>> m = p.match('a\nb')
  >>> print(m) </code></pre>
  <re.Match object; span=(0, 3), match='a\nb'>
    
 #### IGNORECASE, I
 <code>re.IGNORECASE</code> 또는 <code>re.I</code> 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션
 
 <pre><code>>>> p = re.compile('[a-z]+', re.I)
>>> p.match('python')</code></pre>
<re.Match object; span=(0, 6), match='python'>
<pre><code>>> p.match('Python') </code></pre>
<re.Match object; span=(0, 6), match='Python'>
<pre><code>>> p.match('PYTHON') </code></pre>
<re.Match object; span=(0, 6), match='PYTHON'><p>
-> [a-z]+ 정규식은 소문자만을 의미, re.l 옵션으로 대소문자 구별없이 매치된다.
   
#### MULTILINE, M
  <code>re.MULTILINE</code> 또는 <code>re.M</code> 옵션은 <code>^</code>,<code>$</code> 와 연관된 옵션이다.<p>
  <code>^</code> 은 문자열 처음을 의미, <code>$</code>는 문자열 마지막을 의미<p>
<pre><code>>>> import re
>>> p = re.compile("^python\s\w+")

>>> data = """python one
>>> life is too short
>>> python two
>>> you need python
>>> python three"""

>>> print(p.findall(data)) </code></pre>  
['python one']<p>
-> <code>^</code>메타문자에 의해 python이라는 문자열을 사용한 첫 번째 줄만 매치된 것<p>

<code>^</code>메타문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶을 경우
<pre><code>>>> import re
>>> p = re.compile("^python\s\w+", re.MULTILINE)

>>> data = """python one
>>> life is too short
>>> python two
>>> you need python
>>> python three"""

>>> print(p.findall(data)) </code></pre>  
['python one', 'python two', 'python three']

#### VERBOSE, X
  이해하기 어려운 정규식을 주석 또는 줄 단위로 구분하는 방법<p>
  <code>re.VERBOSE</code> 또는 <code>re.X</code> 
<pre><code>>> charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);') </code></pre>  
<pre><code>>> charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)</code></pre>   

첫번째와 두번째 예를 비교하면 컴파일 된 패턴 객체인 charref는 모두 동일한 역할을 한다. 하지만 정규식이 복잡한 경우 두번째 처럼 주석을 적고 여러 줄로 표현하는 것이 훨씬 가독성이 좋다는 것을 알 수 있다. 
  
### ■ 백슬래시 문제
<pre><code> \section </code></pre>
이 정규식은   <code>>> \s </code>문자가 whitespace로 해석되어 의도한대로 매치 x
  
<pre><code> [ \t\n\r\f\v]ection </code></pre>
  
과 동일한 의미이다. 의도한 대로 매치하고 싶으면 
<pre><code> \\section </code></pre>
  
컴파일할려면 
  
<pre><code>>> p = re.compile('\\section') </code></pre> 
  
-> 정규식 엔진에서 \\을 보낼려면 파이썬은 \\\\처럼 백슬래시 4개를 사용해야함 <p>

