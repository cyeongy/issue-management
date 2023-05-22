1. 다운 받아야하는 이미지

- k3s-airgap-images-amd64.tar.gz
- install.sh
- k3s

2. 이미지 다운로드

```bash
sudo mkdir -p /var/lib/rancher/k3s/agent/images/
sudo cp ./k3s-airgap-images-amd64.tar /var/lib/rancher/k3s/agent/images/
```

3. 바이너리 저장

```bash
chmod +x ./k3s
sudo cp ./k3s /usr/local/bin
```

4. K3s 인스톨

```bash
sudo INSTALL_K3S_SKIP_DOWNLOAD=true ./install.sh
```
