FROM public.ecr.aws/docker/library/python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#requirements.txt에 파이썬 라이브러리 설치파일들이 들어있다.

CMD ["uvicorn","main:app","--host","0.0.0.0"]
