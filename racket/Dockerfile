FROM public.ecr.aws/lambda/python:3.13

RUN dnf install -y tar

RUN curl -L -o racket.sh https://mirror.racket-lang.org/installers/8.16/racket-8.16-x86_64-linux.sh && \
  chmod +x racket.sh && \
  ./racket.sh --in-place --dest /opt/racket && \
  ln -s /opt/racket/bin/racket /usr/local/bin/racket && \
  rm racket.sh

COPY lambda_function.py ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.lambda_handler"]