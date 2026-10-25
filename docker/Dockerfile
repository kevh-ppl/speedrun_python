FROM python:3.12-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PS1='\[\e[1;33m\]speedrun-py\[\e[0m\]:\[\e[1;34m\]\w\[\e[0m\]$ '

RUN apt-get update && apt-get install -y --no-install-recommends \
      bash \
      bash-completion \
      coreutils \
      findutils \
      grep \
      sed \
      gawk \
      jq \
      file \
      tree \
      less \
      vim-tiny \
      nano \
      git \
      curl \
      ca-certificates \
      make \
      procps \
      psmisc \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
      pytest==8.3.3 \
      pytest-timeout==2.3.1 \
      ruff==0.6.9 \
      mypy==1.11.2

# Usuario no-root
RUN useradd -m -s /bin/bash lab
USER lab
WORKDIR /lab

CMD ["bash"]
