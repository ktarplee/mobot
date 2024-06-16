# Calvin's mobot

## Setup

Run `raspi-config` to enable the i2c interface which is needed for the servo controller.

Install direnv and set it up

```bash
sudo apt install direnv
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
```

Clone the repo and enable envrc

```bash
git clone git@github.com:ktarplee/mobot.git
cd mobot
direnv allow .
```

```bash
sudo apt install python3-dev
pip install -r requirements.txt
```

## Running Servo Controller

```bash
python main.py
```

## Camera

Install camera drivers with `sudo apt install libraspberrypi-bin`.

Then capture images with `rpicam-jpeg --output ~/test.jpg`.

## Troubleshooting

```bash
sudo apt-get install i2c-tools
i2cdetect -y 1
```

Ensure that 0x40 shows up.
