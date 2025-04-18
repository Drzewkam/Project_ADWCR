{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5576319-4692-4571-bd01-ac8b54eddb53",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"Witaj w moim API!\"\n",
    "\n",
    "@app.route('/hello/<name>')\n",
    "def hello(name):\n",
    "    return f\"Cześć, {name}!\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "769a2b1e-52c3-49c1-b0e5-1ac282c83fe3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "resp = requests.get(\"http://127.0.0.1:5000/hello/Adam\")\n",
    "assert resp.status_code == 200\n",
    "print(resp.text)  # Cześć, Adam!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
