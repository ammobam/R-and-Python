#R에서의 Factor는 범주, 카테고리
#level이 있는 학점, 금은동 등의 기호를 Factor로 받아들임
stringsAsFactors = F

#--------------------------
#텍스트 파일 읽기

ex1<- read.table("data.txt")
setwd("c:/Rdata/")
#이 두 줄은 아래 한 줄로도 가능.
#ex1<- read.table("c:/Rdata/data.txt")
##근데 같은 파일 소환에도매번 c:/.. 적어야됨.

View(ex1)
colnames("ex1")

ex2 <- read.table("data.txt", header=TRUE)
View(ex2)

#데이터 저장 방법
write.table(ex2, "data1.txt")

#------------------------
#------------------------
x1<- 1:20
x2<- rep(c("a", "b"), 10)
  #replicate 복제. "a","b"를 하나로 묶어서(combine) 10번 복제

x3<- sample(1:100, 20)
  #1부터 100까지 중에 표본(sample) 20개 뽑기

sample(1:10, 20)
  #모집단보다 큰 표본 추출은 오류가 난다
sample(1:10, 20, replace=T)
  #복원추출

data1<-cbind(x1, x2, x3)
  #column
rbind()
  #row
class(data1)
df<-  as.data.frame(data1)
  #모든 데이터는 데이터프레임으로 바꾼 다음 저장한다
write.table(df, "text.txt")
  #df를 text.txt라는 이름으로 저장함
  #파일 열어보면 "a" "b" 식으로 스페이스로 데이터 구분함
write.table(df, "text.txt", sep=",")
  #파일 열어보면 "a","b" 식으로 ","로 데이터 구분함
write.table(df, "text.txt", sep="\t")
  #파일 열어보면 "a"  "b" 식으로 tab으로 데이터 구분함


#------------------------
#csv 파일 읽기, 저장하기
read.table("text.txt")

txt <-read.table("text.txt", header = T)

write.csv(df, "data.csv")
read.csv("data.csv")


  
  
  
  
  
