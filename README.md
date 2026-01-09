# 🚫 Rejection as a Service (RaaS)

**Rejection as a Service (RaaS)** is a mission-critical API designed to handle your inability to say "No."

In today's fast-paced environment, protecting your time is paramount. Why rely on manual, emotionally draining refusals when you can automate your boundaries with enterprise-grade reliability? RaaS delivers randomized, context-free rejections in both English and German, ensuring you never have to commit to anything ever again.

## ✨ Key Features

* **Scalable Denial:** Capable of rejecting thousands of requests per second.
* **Multi-Locale Support:** Native rejections in English (`en`) and German (`de`).
* **Stateless Architecture:** We don't remember who asked, and we don't care.
* **Lightweight Core:** Built on Flask, running with zero heavy dependencies.

## 🚀 Installation

### Prerequisites
* Python 3.x
* A desire to be left alone

### Setup
1.  Clone the repository:
    ```bash
    git clone https://github.com/nullr0uter/RejectAsAService.git
    cd RejectAsAService
    ```

2.  Install dependencies:
    ```bash
    pip install Flask
    ```

## 🛠 Usage

Start the service using the provided Python script. By default, it runs on `127.0.0.1:5000`.

```bash
python Service.py

```

### Configuration

You can customize the host and port using command-line arguments:

| Argument | Default | Description |
| --- | --- | --- |
| `--host` | `127.0.0.1` | The interface to bind the service to. |
| `--port` | `5000` | The port to listen on. |
| `--debug` | `False` | Enable debug mode for verbose rejection logs. |

**Example:**

```bash
python Service.py --port 8080 --debug

```

## 🔌 API Reference

### 1. Root Check

Verifies the service is running and reminds you to choose a language.

* **Endpoint:** `GET /`
* **Response:**
```json
{
  "culture": "Please choose /de or /en"
}

```



### 2. English Rejection

Returns a randomly selected refusal from a file with English rejections.

* **Endpoint:** `GET /en`
* **Example Response:**
```json
{
  "reason": "Not today."
}

```



### 3. German Rejection

Returns a randomly selected refusal from a file with German rejections.

* **Endpoint:** `GET /de`
* **Example Response:**
```json
{
  "reason": "Heute sage ich nein, damit morgen nichts brennt."
}

```



## 🤝 Contributing

We are currently **not** accepting contributions. Please consider this sentence our first service demonstration.
*(Just kidding—feel free to open a PR if you have better excuses to add to `rejections_*.txt`).*

## 📜 Acknowledgements

Inspired by [No as a Service](https://github.com/hotheadhacker/no-as-a-service)
