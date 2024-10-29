#git clone https://github.com/themoka7/myload.git myloadgit
#rsync -avh --exclude='.git' myloadgit/ ./
#그 이후 소스 가져오기
cd /home/kimjungmok/mysite/myloadgit
git pull origin main
cd ..
rsync -avh --exclude='.git' myloadgit/ ./