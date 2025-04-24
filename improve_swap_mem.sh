## Since I was working on a laptop with 4GB of RAM, 2GB of Swap and running Ubuntu 20.04 with no GPU, It was a herculean task to be able to run even the smallest of LLMs on my system.
## To conquer that, I added extra 8GB of swap memory using the following code. Then I ran Ollama phi3 model locally. It was working perfectly fine, just quite slow.

sudo fallocate -l 8G /swapfile-extra
sudo chmod 600 /swapfile-extra
sudo mkswap /swapfile-extra
sudo swapon /swapfile-extra