#--------------------------
#행렬만들기
matl <- matrix(1:12)

#3행4열 만들기
mat2 <- matrix(1:12, nrow=3, ncol=4)

#행과 열 전환하기
mat3 <- matrix(1:12, nrow=3, byrow=1)
##mat1, mat2, mat3 타이핑하지 말고 윗줄 일부 드래그 해서 실행 가능
matrix(1:12, 3, byrow=T)

#행렬에 이름붙이기
##행 개수와 동일한 개수의 이름을 combine함수로 묶어서 부여
rownames(mat3) <- c("국어", "영어", "수학")
colnames(mat3) <- c("a1", "a2", "a3", "a4")

ls()
rm()
#ls()한번에 초기화 하는 방법?
help(rm)
?rm()
rm #쓰고 키보드 F1, F2
  ##오픈소스라 코드를 볼 수 있음
  ##remove {base}
help(ggplot)
  ##ggplot {ggplot2} // 이름{패키지 위치}
  ##Arguments/Examples를 살펴보자

rm(list=ls())
ls()

#--------------------------
mat3 <- matrix(1:12, nrow=3, byrow=1)
##byrow = F 가 기본값(Default)으로, (1,1),(1,2).. 순으로 항목을 채움
## http://www.datamarket.kr/xe/index.php?mid=board_ecko11&document_srl=411&listStyle=viewer
##mat1, mat2, mat3 타이핑하지 말고 윗줄 일부 드래그 해서 실행 가능
matrix(1:12, 3, byrow=T)

#행렬에 이름붙이기
##행 개수와 동일한 개수의 이름을 combine함수로 묶어서 부여
rownames(mat3) <- c("국어", "영어", "수학")
colnames(mat3) <- c("a1", "a2", "a3", "a4")

mat3[2,3]   ##2행 3열
mat<-mat3   ##행렬명 변경
rm(mat3)

mat[1,1]    ##R은 1부터 시작함
mat[2, ]
mat[ ,4]
mat[ ,-3]   ##해당 열을 뺌
mat[-1,-1]
mat["국어",]##행렬명으로도 가능
mat[ ,2:4]  ##행 전체, 2~4열
mat[ ,c(2,4)]
mat[ ,c("a2","a4")]

#대각행렬(transposed)
t(mat)

#--------------------------

x1<- c(100, 80, 60, 40, 30)
x2<- c("A","B","C","A","B")

data.frame(x1, x2)
##이렇게는 화면에 출력하기만 하고 저장하지 않은 것. df에 저장하자.
df<-data.frame(x1, x2)
df
df<-data.frame(score=x1, grade=x2)
##왼쪽에 new one, 오른쪽에 old one 순으로 이름 붙인다.
##=를 <-로 바꾸면 이름이...??

df[, 1]
df$score
df$grade
  
