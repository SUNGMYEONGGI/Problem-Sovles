# [level 0] 특이한 정렬 - 120880 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120880) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 05월 01일 19:24:31

### 문제 설명

<p style="user-select: auto !important;">정수 <code style="user-select: auto !important;">n</code>을 기준으로 <code style="user-select: auto !important;">n</code>과 가까운 수부터 정렬하려고 합니다. 이때 <code style="user-select: auto !important;">n</code>으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 <code style="user-select: auto !important;">numlist</code>와 정수 <code style="user-select: auto !important;">n</code>이 주어질 때 <code style="user-select: auto !important;">numlist</code>의 원소를 <code style="user-select: auto !important;">n</code>으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">n</code> ≤ 10,000</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">numlist</code>의 원소 ≤ 10,000</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">numlist</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">numlist</code>는 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">numlist</th>
<th style="user-select: auto !important;">n</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[1, 2, 3, 4, 5, 6]</td>
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">[4, 5, 3, 6, 2, 1]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[10000,20,36,47,40,6,10,7000]</td>
<td style="user-select: auto !important;">30</td>
<td style="user-select: auto !important;">[36, 40, 20, 47, 10, 6, 7000, 10000]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">4에서 가까운 순으로 [4, 5, 3, 6, 2, 1]을 return합니다.</li>
<li style="user-select: auto !important;">3과 5는 거리가 같으므로 더 큰 5가 앞에 와야 합니다.</li>
<li style="user-select: auto !important;">2와 6은 거리가 같으므로 더 큰 6이 앞에 와야 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">30에서 가까운 순으로 [36, 40, 20, 47, 10, 6, 7000, 10000]을 return합니다.</li>
<li style="user-select: auto !important;">20과 40은 거리가 같으므로 더 큰 40이 앞에 와야 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges