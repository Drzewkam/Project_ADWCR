{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2367ea07-122a-49fc-a7b6-0c308ed05430",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"Witaj w moim API!\"\n",
    "\n",
    "@app.route('/add')\n",
    "def add():\n",
    "    a = request.args.get('a', type=float, default=0)\n",
    "    b = request.args.get('b', type=float, default=0)\n",
    "    return str(a + b)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bedb705b-d21e-47f6-9bb4-1f92215aaa85",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "resp = requests.get(\"http://127.0.0.1:5000/add\", params={\"a\": 3.5, \"b\": 4.2})\n",
    "assert resp.status_code == 200\n",
    "print(resp.text)  # 7.7\n"
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
