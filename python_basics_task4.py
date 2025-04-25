{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Abdallah943/AI_Python_basic-/blob/main/python_basics_task4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "759d04ba",
      "metadata": {
        "id": "759d04ba"
      },
      "source": [
        "**1-Write a Python program to calculate the length of a string using 2 ways"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e434c950",
      "metadata": {
        "id": "e434c950",
        "outputId": "6c0f71c8-9a35-483d-a163-76b6b2d0f19f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Length using while loop: 7\n"
          ]
        }
      ],
      "source": [
        "text = \"example\"\n",
        "count = 0\n",
        "while count < 1000:\n",
        "    try:\n",
        "        text[count]\n",
        "        count = count + 1\n",
        "    except:\n",
        "        break\n",
        "print(\"Length using while loop:\", count)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7a2dfa32",
      "metadata": {
        "id": "7a2dfa32",
        "outputId": "efd3a589-f8cf-466f-a312-c2f73f93068a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Length using for loop: 7\n"
          ]
        }
      ],
      "source": [
        "text = \"example\"\n",
        "count = 0\n",
        "for char in text:\n",
        "    count = count + 1\n",
        "print(\"Length using for loop:\", count)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "d7cc9da7",
      "metadata": {
        "id": "d7cc9da7"
      },
      "source": [
        "**2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead (\"##Sample String : 'w3resource'\n",
        "Expected Result : 'w3ce'\n",
        "##Sample String : 'w3'\n",
        "Expected Result : 'w3w3'\n",
        "##Sample String : ' w'\n",
        "Expected Result : Empty String)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "dafa9dd8",
      "metadata": {
        "id": "dafa9dd8",
        "outputId": "f48eeee6-ec12-4026-b60a-e8c2a73b7592",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "w3ce\n"
          ]
        }
      ],
      "source": [
        "text = \"w3resource\"\n",
        "count = 0\n",
        "for char in text:\n",
        "    count += 1\n",
        "\n",
        "if count < 2:\n",
        "    print(\"\")\n",
        "else:\n",
        "    first = text[0] + text[1]\n",
        "    last = text[count - 2] + text[count - 1]\n",
        "    print(first + last)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "1534f956",
      "metadata": {
        "id": "1534f956"
      },
      "source": [
        "**3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. (Sample String : 'abc'\n",
        "Expected Result : 'abcing')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7ff8cec4",
      "metadata": {
        "id": "7ff8cec4",
        "outputId": "0b7e2598-d484-459a-96aa-c1d4b5d25f99",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "stringly\n"
          ]
        }
      ],
      "source": [
        "text = \"string\"\n",
        "count = 0\n",
        "for char in text:\n",
        "    count += 1\n",
        "\n",
        "if count < 3:\n",
        "    print(text)\n",
        "elif text[count - 3] == 'i' and text[count - 2] == 'n' and text[count - 1] == 'g':\n",
        "    print(text + \"ly\")\n",
        "else:\n",
        "    print(text + \"ing\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "1c0a6627",
      "metadata": {
        "id": "1c0a6627"
      },
      "source": [
        "**4-Write a Python function that takes a list of words and return the longest word and the length of the longest one\n",
        "(Longest word: Exercises\n",
        "Length of the longest word: 9)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "397341d9",
      "metadata": {
        "id": "397341d9",
        "outputId": "e1ba7c90-53cc-4918-813f-e71f8334d416",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Longest word: Programming\n",
            "Length of the longest word: 11\n"
          ]
        }
      ],
      "source": [
        "def longest_word(words):\n",
        "    max_len = 0\n",
        "    longest = \"\"\n",
        "    for word in words:\n",
        "        length = 0\n",
        "        for char in word:\n",
        "            length += 1\n",
        "        if length > max_len:\n",
        "            max_len = length\n",
        "            longest = word\n",
        "    print(\"Longest word:\", longest)\n",
        "    print(\"Length of the longest word:\", max_len)\n",
        "\n",
        "word_list = [\"Python\", \"Exercises\", \"Programming\"]\n",
        "longest_word(word_list)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "53a03a6a",
      "metadata": {
        "id": "53a03a6a"
      },
      "source": [
        "**5-Write a Python program to change a given string to a newly string where the first and last chars have been exchanged using 2 ways (Sample String:abca  Expected Result:ebce)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fd327d2a",
      "metadata": {
        "id": "fd327d2a",
        "outputId": "dd64ade4-b2d0-4960-99ea-68eb3b101a11",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "abca\n"
          ]
        }
      ],
      "source": [
        "# Method 1: Using indexing\n",
        "text = \"abca\"\n",
        "count = 0\n",
        "for char in text:\n",
        "    count += 1\n",
        "\n",
        "if count >= 2:\n",
        "    new_string = text[count - 1]\n",
        "    for i in range(1, count - 1):\n",
        "        new_string += text[i]\n",
        "    new_string += text[0]\n",
        "    print(new_string)\n",
        "else:\n",
        "    print(text)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "285788b4",
      "metadata": {
        "id": "285788b4",
        "outputId": "aebff210-b13a-43f7-eac6-47378cde7ab8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "abca\n"
          ]
        }
      ],
      "source": [
        "# Method 2: Using while loop\n",
        "text = \"abca\"\n",
        "count = 0\n",
        "for char in text:\n",
        "    count += 1\n",
        "\n",
        "if count >= 2:\n",
        "    i = 1\n",
        "    new_string = text[count - 1]\n",
        "    while i < count - 1:\n",
        "        new_string += text[i]\n",
        "        i += 1\n",
        "    new_string += text[0]\n",
        "    print(new_string)\n",
        "else:\n",
        "    print(text)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "25f89808",
      "metadata": {
        "id": "25f89808"
      },
      "source": [
        "**6-Write a Python program to remove characters that have odd index values in a given string (Sample String:abca Expected Result:ac)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "05959bd7",
      "metadata": {
        "id": "05959bd7",
        "outputId": "e309fd38-2843-49f9-bd2f-d2076eb2f989",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ac\n"
          ]
        }
      ],
      "source": [
        "text = \"abca\"\n",
        "new_text = \"\"\n",
        "index = 0\n",
        "for char in text:\n",
        "    if index % 2 == 0:\n",
        "        new_text += char\n",
        "    index += 1\n",
        "print(new_text)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "eb16e898",
      "metadata": {
        "id": "eb16e898"
      },
      "source": [
        "**7-Write a Python program to count the occurrences of each word in a given sentence (Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "01ce6cf5",
      "metadata": {
        "id": "01ce6cf5",
        "outputId": "467973ee-0a5f-4126-f422-7f467c79580b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "amr: 2\n",
            "and: 1\n",
            "ahmed: 1\n",
            "are: 1\n",
            "friends: 1\n",
            "but: 1\n",
            "is: 1\n",
            "the: 1\n",
            "tallest: 1\n"
          ]
        }
      ],
      "source": [
        "sentence = \"amr and ahmed are friends but amr is the tallest\"\n",
        "words = []\n",
        "word = \"\"\n",
        "for char in sentence:\n",
        "    if char != \" \":\n",
        "        word += char\n",
        "    else:\n",
        "        if word != \"\":\n",
        "            words.append(word)\n",
        "            word = \"\"\n",
        "if word != \"\":\n",
        "    words.append(word)\n",
        "\n",
        "counts = []\n",
        "for i in range(len(words)):\n",
        "    current_word = words[i]\n",
        "    count = 0\n",
        "    for j in range(len(words)):\n",
        "        if words[j] == current_word:\n",
        "            count += 1\n",
        "    found = False\n",
        "    for k in range(i):\n",
        "        if words[k] == current_word:\n",
        "            found = True\n",
        "            break\n",
        "    if not found:\n",
        "        print(current_word + \":\", count)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "4e8125f1",
      "metadata": {
        "id": "4e8125f1"
      },
      "source": [
        "**8-Write a Python script that takes input from the user and displays that input back in upper and lower cases"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "66c8f778",
      "metadata": {
        "id": "66c8f778",
        "outputId": "3e9edb8f-7230-4e20-85ba-f9b53d9c64d7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter text: tyuui\n",
            "Upper case: TYUUI\n",
            "Lower case: tyuui\n"
          ]
        }
      ],
      "source": [
        "text = input(\"Enter text: \")\n",
        "\n",
        "# Upper case\n",
        "upper_text = \"\"\n",
        "for char in text:\n",
        "    if 'a' <= char <= 'z':\n",
        "        upper_text += chr(ord(char) - 32)\n",
        "    else:\n",
        "        upper_text += char\n",
        "\n",
        "# Lower case\n",
        "lower_text = \"\"\n",
        "for char in text:\n",
        "    if 'A' <= char <= 'Z':\n",
        "        lower_text += chr(ord(char) + 32)\n",
        "    else:\n",
        "        lower_text += char\n",
        "\n",
        "print(\"Upper case:\", upper_text)\n",
        "print(\"Lower case:\", lower_text)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "fcd68aa1",
      "metadata": {
        "id": "fcd68aa1"
      },
      "source": [
        "**9-Write a Python function to reverse a string if its length is a multiple of 4"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0671a931",
      "metadata": {
        "id": "0671a931",
        "outputId": "57907904-f7ff-48d9-e8c2-6be820b9d0bc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "zyxwdcba\n"
          ]
        }
      ],
      "source": [
        "text = \"abcdwxyz\"\n",
        "length = 0\n",
        "for char in text:\n",
        "    length += 1\n",
        "\n",
        "if length % 4 == 0:\n",
        "    reversed_text = \"\"\n",
        "    index = length - 1\n",
        "    while index >= 0:\n",
        "        reversed_text += text[index]\n",
        "        index -= 1\n",
        "    print(reversed_text)\n",
        "else:\n",
        "    print(text)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b577c68d",
      "metadata": {
        "id": "b577c68d"
      },
      "source": [
        "**10- Write a Python program to remove a newline in Python"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e0c6525a",
      "metadata": {
        "id": "e0c6525a",
        "outputId": "6fad09a4-1261-45fd-dc4c-262e7e43ce74",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Text without newline: hello world\n"
          ]
        }
      ],
      "source": [
        "text = \"hello world\\n\"\n",
        "new_text = \"\"\n",
        "length = 0\n",
        "for char in text:\n",
        "    length += 1\n",
        "\n",
        "if text[length - 1] == '\\n':\n",
        "    for i in range(length - 1):\n",
        "        new_text += text[i]\n",
        "else:\n",
        "    new_text = text\n",
        "\n",
        "print(\"Text without newline:\", new_text)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "80db5ae0",
      "metadata": {
        "id": "80db5ae0"
      },
      "source": [
        "**11-Write a Python program to check whether a string starts with specified characters"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0cc4e03e",
      "metadata": {
        "id": "0cc4e03e",
        "outputId": "94266dfc-41c3-49be-ac9d-e4eed6060d76",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Yes, starts with: he\n"
          ]
        }
      ],
      "source": [
        "# Check if string starts with specific characters without using built-in functions\n",
        "\n",
        "string = \"hello world\"\n",
        "start = \"he\"\n",
        "\n",
        "match = True\n",
        "for i in range(len(start)):\n",
        "    if i >= len(string) or string[i] != start[i]:\n",
        "        match = False\n",
        "        break\n",
        "\n",
        "if match:\n",
        "    print(\"Yes, starts with:\", start)\n",
        "else:\n",
        "    print(\"No, does not start with:\", start)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "593a68db",
      "metadata": {
        "id": "593a68db"
      },
      "source": [
        "**12- Write a Python program to add prefix text to all of the lines in a string"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d2e46ada",
      "metadata": {
        "id": "d2e46ada",
        "outputId": "08f9af8a-e761-4902-cac8-2ed2fa2dfbaa",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--> first line\n",
            "--> second line\n",
            "--> third line\n",
            "\n"
          ]
        }
      ],
      "source": [
        "# Add prefix to each line in a string\n",
        "\n",
        "text = \"first line\\nsecond line\\nthird line\"\n",
        "prefix = \"--> \"\n",
        "\n",
        "lines = text.split(\"\\n\")\n",
        "result = \"\"\n",
        "for line in lines:\n",
        "    result += prefix + line + \"\\n\"\n",
        "\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "86fa1543",
      "metadata": {
        "id": "86fa1543"
      },
      "source": [
        "**13-Write a Python program to print the following numbers up to 2 decimal places"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "cd4a9d89",
      "metadata": {
        "id": "cd4a9d89",
        "outputId": "21c7d311-8687-4b1b-fbda-ddb5a1df0a81",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.14\n"
          ]
        }
      ],
      "source": [
        "# Print number with 2 decimal places\n",
        "\n",
        "number = 3.14159\n",
        "multiplied = int(number * 100)\n",
        "result = multiplied / 100.0\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "452c0ab0",
      "metadata": {
        "id": "452c0ab0"
      },
      "source": [
        "**14-Write a Python program to print the following numbers up to 2 decimal places with a sign"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "73e82479",
      "metadata": {
        "id": "73e82479",
        "outputId": "1d5c3cc9-8752-4cd1-c806-d6af1e120e0e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-3.14\n"
          ]
        }
      ],
      "source": [
        "# Print number with 2 decimals and sign\n",
        "\n",
        "number = -3.14159\n",
        "multiplied = int(abs(number) * 100)\n",
        "result = multiplied / 100.0\n",
        "\n",
        "if number >= 0:\n",
        "    print(\"+\" + str(result))\n",
        "else:\n",
        "    print(\"-\" + str(result))\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "32b1811a",
      "metadata": {
        "id": "32b1811a"
      },
      "source": [
        "**15-Write a Python program to display a number with a comma separator"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f30fc0b6",
      "metadata": {
        "id": "f30fc0b6",
        "outputId": "ce6aecbb-52f8-4237-d154-7b9f9310b8c5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1,234,567\n"
          ]
        }
      ],
      "source": [
        "# Display number with comma separator\n",
        "\n",
        "number = 1234567\n",
        "number_str = str(number)\n",
        "result = \"\"\n",
        "count = 0\n",
        "\n",
        "for i in range(len(number_str)-1, -1, -1):\n",
        "    result = number_str[i] + result\n",
        "    count += 1\n",
        "    if count % 3 == 0 and i != 0:\n",
        "        result = \",\" + result\n",
        "\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "0477f487",
      "metadata": {
        "id": "0477f487"
      },
      "source": [
        "**16-Write a Python program to reverse a string using 2 ways"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "aa8beec8",
      "metadata": {
        "id": "aa8beec8",
        "outputId": "80272b9c-a5d5-4b46-9959-b83631a087be",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "olleh\n",
            "olleh\n"
          ]
        }
      ],
      "source": [
        "# Method 1: using loop\n",
        "text = \"hello\"\n",
        "reversed1 = \"\"\n",
        "for i in range(len(text)-1, -1, -1):\n",
        "    reversed1 += text[i]\n",
        "print(reversed1)\n",
        "\n",
        "# Method 2: using manual swap\n",
        "text_list = list(text)\n",
        "start = 0\n",
        "end = len(text_list) - 1\n",
        "while start < end:\n",
        "    temp = text_list[start]\n",
        "    text_list[start] = text_list[end]\n",
        "    text_list[end] = temp\n",
        "    start += 1\n",
        "    end -= 1\n",
        "print(\"\".join(text_list))\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "5afc3166",
      "metadata": {
        "id": "5afc3166"
      },
      "source": [
        " **17-Write a Python program to count repeated characters in a string (hint:use dictionary)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "515a469c",
      "metadata": {
        "id": "515a469c",
        "outputId": "4a54461d-a8db-4ffa-c4b0-69cbad27e4a8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i : 4\n",
            "s : 4\n",
            "p : 2\n"
          ]
        }
      ],
      "source": [
        "# Count repeated characters in a string\n",
        "\n",
        "text = \"mississippi\"\n",
        "char_count = {}\n",
        "\n",
        "for ch in text:\n",
        "    if ch in char_count:\n",
        "        char_count[ch] += 1\n",
        "    else:\n",
        "        char_count[ch] = 1\n",
        "\n",
        "for ch in char_count:\n",
        "    if char_count[ch] > 1:\n",
        "        print(ch, \":\", char_count[ch])\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "ae14e4e5",
      "metadata": {
        "id": "ae14e4e5"
      },
      "source": [
        "**18-Write a Python program to find the first non-repeating character in a given string"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d73778e5",
      "metadata": {
        "id": "d73778e5",
        "outputId": "19a2b043-59c4-4cac-e0c9-c021da2dcf16",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First non-repeating character: c\n"
          ]
        }
      ],
      "source": [
        "# First non-repeating character\n",
        "\n",
        "text = \"aabbcddee\"\n",
        "char_count = {}\n",
        "\n",
        "for ch in text:\n",
        "    if ch in char_count:\n",
        "        char_count[ch] += 1\n",
        "    else:\n",
        "        char_count[ch] = 1\n",
        "\n",
        "for ch in text:\n",
        "    if char_count[ch] == 1:\n",
        "        print(\"First non-repeating character:\", ch)\n",
        "        break\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3adf5669",
      "metadata": {
        "id": "3adf5669"
      },
      "source": [
        "**19-Write a Python program to remove spaces from a given string"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b4f22602",
      "metadata": {
        "id": "b4f22602",
        "outputId": "25cd7b73-68b0-4350-98f9-0769018ac5bc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "abcde\n"
          ]
        }
      ],
      "source": [
        "# Remove all spaces from string\n",
        "\n",
        "text = \"a b c d e\"\n",
        "result = \"\"\n",
        "\n",
        "for ch in text:\n",
        "    if ch != \" \":\n",
        "        result += ch\n",
        "\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "734de60c",
      "metadata": {
        "id": "734de60c"
      },
      "source": [
        "**20-Write a Python program to count the number of non-empty substrings of a given string"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ef3f2274",
      "metadata": {
        "id": "ef3f2274",
        "outputId": "e8b0201a-53c8-4bb5-e984-baf5021dcff6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of non-empty substrings: 10\n"
          ]
        }
      ],
      "source": [
        "# Count non-empty substrings\n",
        "\n",
        "text = \"abcd\"\n",
        "length = len(text)\n",
        "count = 0\n",
        "\n",
        "for i in range(length):\n",
        "    for j in range(i+1, length+1):\n",
        "        count += 1  # text[i:j] is a non-empty substring\n",
        "\n",
        "print(\"Number of non-empty substrings:\", count)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "509998e2",
      "metadata": {
        "id": "509998e2"
      },
      "source": [
        "**21-write a Python program to swap first and last element of any list."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "68692d7f",
      "metadata": {
        "id": "68692d7f",
        "outputId": "e2f93c0c-c62b-4b4a-f51c-66d16e1056aa",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5, 2, 3, 4, 1]\n"
          ]
        }
      ],
      "source": [
        "# Swap first and last element in a list\n",
        "\n",
        "lst = [1, 2, 3, 4, 5]\n",
        "\n",
        "if len(lst) > 1:\n",
        "    temp = lst[0]\n",
        "    lst[0] = lst[-1]\n",
        "    lst[-1] = temp\n",
        "\n",
        "print(lst)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "959e0837",
      "metadata": {
        "id": "959e0837"
      },
      "source": [
        "**22-Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. (Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3\n",
        "Output : [19, 65, 23, 90])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "225d8c6d",
      "metadata": {
        "id": "225d8c6d",
        "outputId": "298d266a-1a31-4def-d2ec-6d61ecb88b23",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[23, 90, 19, 65]\n"
          ]
        }
      ],
      "source": [
        "# Swap two elements in a list based on positions\n",
        "\n",
        "lst = [23, 65, 19, 90]\n",
        "pos1 = 1\n",
        "pos2 = 3\n",
        "\n",
        "lst[pos1], lst[pos2] = lst[pos2], lst[pos1]\n",
        "\n",
        "print(lst)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "66fc6682",
      "metadata": {
        "id": "66fc6682"
      },
      "source": [
        "**23- search for the all ways to know the length of the list"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Different ways to find the length of a list\n",
        "\n",
        "lst = [10, 20, 30, 40]\n",
        "\n",
        "# Method 1: Using len()\n",
        "print(\"Length using len():\", len(lst))\n",
        "\n",
        "# Method 2: Using loop\n",
        "count = 0\n",
        "for _ in lst:\n",
        "    count += 1\n",
        "print(\"Length using loop:\", count)\n",
        "\n",
        "# Method 3: Using enumerate\n",
        "print(\"Length using enumerate:\", list(enumerate(lst))[-1][0] + 1)\n"
      ],
      "metadata": {
        "id": "zQ5ASG6n8Ibw",
        "outputId": "a708dee0-b576-4830-c6d6-62c3750de5dc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "id": "zQ5ASG6n8Ibw",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Length using len(): 4\n",
            "Length using loop: 4\n",
            "Length using enumerate: 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**24-write a Python code to find the Maximum number of list of numbers."
      ],
      "metadata": {
        "id": "UzDLVwCV8Uou"
      },
      "id": "UzDLVwCV8Uou"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "15f342de",
      "metadata": {
        "id": "15f342de",
        "outputId": "7478f16c-aaa8-4be8-dfbb-2193a0ee2475",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Max number: 19\n"
          ]
        }
      ],
      "source": [
        "# Find max number in a list\n",
        "\n",
        "lst = [4, 12, 7, 19, 3]\n",
        "max_num = lst[0]\n",
        "\n",
        "for num in lst:\n",
        "    if num > max_num:\n",
        "        max_num = num\n",
        "\n",
        "print(\"Max number:\", max_num)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**25-write a Python code to find the Minimum number of list of numbers."
      ],
      "metadata": {
        "id": "6qsFbIA18ZRQ"
      },
      "id": "6qsFbIA18ZRQ"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "21f8cbd6",
      "metadata": {
        "id": "21f8cbd6",
        "outputId": "c8451564-0f8c-4801-8d0d-2418031ddd5d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Min number: 3\n"
          ]
        }
      ],
      "source": [
        "# Find min number in a list\n",
        "\n",
        "lst = [4, 12, 7, 19, 3]\n",
        "min_num = lst[0]\n",
        "\n",
        "for num in lst:\n",
        "    if num < min_num:\n",
        "        min_num = num\n",
        "\n",
        "print(\"Min number:\", min_num)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "96822d96",
      "metadata": {
        "id": "96822d96"
      },
      "source": [
        "**26-search for if an elem is existing in list"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "51ca5c9a",
      "metadata": {
        "id": "51ca5c9a",
        "outputId": "9b96d19b-8d8a-41c7-ceea-2ecaafe89656",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20 exists in the list.\n"
          ]
        }
      ],
      "source": [
        "# Check if element exists in list\n",
        "\n",
        "lst = [10, 20, 30, 40]\n",
        "x = 20\n",
        "\n",
        "found = False\n",
        "for item in lst:\n",
        "    if item == x:\n",
        "        found = True\n",
        "        break\n",
        "\n",
        "if found:\n",
        "    print(x, \"exists in the list.\")\n",
        "else:\n",
        "    print(x, \"does not exist in the list.\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "d9557da7",
      "metadata": {
        "id": "d9557da7"
      },
      "source": [
        "**27- clear python list using different ways"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b69858a3",
      "metadata": {
        "id": "b69858a3",
        "outputId": "b9d4cf2f-2fc2-4db9-cd5c-ff6e69fd1fd2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[] [] []\n"
          ]
        }
      ],
      "source": [
        "# Clear list using different methods\n",
        "\n",
        "lst1 = [1, 2, 3]\n",
        "lst2 = [4, 5, 6]\n",
        "lst3 = [7, 8, 9]\n",
        "\n",
        "# Method 1: clear()\n",
        "lst1.clear()\n",
        "\n",
        "# Method 2: slice assignment\n",
        "lst2[:] = []\n",
        "\n",
        "# Method 3: del\n",
        "del lst3[:]\n",
        "\n",
        "print(lst1, lst2, lst3)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "52160e88",
      "metadata": {
        "id": "52160e88"
      },
      "source": [
        "**28-remove duplicated elements from a list"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "5e362228",
      "metadata": {
        "id": "5e362228",
        "outputId": "53ae2a63-4dba-4aba-bbfc-f1217b1788ef",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5]\n"
          ]
        }
      ],
      "source": [
        "# Remove duplicates from a list\n",
        "\n",
        "lst = [1, 2, 2, 3, 4, 4, 5]\n",
        "unique = []\n",
        "\n",
        "for item in lst:\n",
        "    if item not in unique:\n",
        "        unique.append(item)\n",
        "\n",
        "print(unique)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "282337f7",
      "metadata": {
        "id": "282337f7"
      },
      "source": [
        "**29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries. (Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]\n",
        "Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "4d4e2d28",
      "metadata": {
        "id": "4d4e2d28",
        "outputId": "f9cc6b32-c364-410d-e550-920b41040247",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[{'name': 'Gfg', 'id': 3}, {'name': 'is', 'id': 8}]\n"
          ]
        }
      ],
      "source": [
        "# Convert list of values and keys to list of dictionaries\n",
        "\n",
        "test_list = [\"Gfg\", 3, \"is\", 8]\n",
        "key_list = [\"name\", \"id\"]\n",
        "result = []\n",
        "\n",
        "for i in range(0, len(test_list), len(key_list)):\n",
        "    sub_dict = {}\n",
        "    for j in range(len(key_list)):\n",
        "        sub_dict[key_list[j]] = test_list[i + j]\n",
        "    result.append(sub_dict)\n",
        "\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "c26b6e9f",
      "metadata": {
        "id": "c26b6e9f"
      },
      "source": [
        "**30-write a python program to count unique values inside a list using different ways"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "72132667",
      "metadata": {
        "id": "72132667",
        "outputId": "a1a3eb37-5027-4ad1-9255-3263631e3735",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Using set: 5\n",
            "Using manual loop: 5\n"
          ]
        }
      ],
      "source": [
        "# Count unique values in a list\n",
        "\n",
        "lst = [1, 2, 2, 3, 4, 4, 5]\n",
        "\n",
        "# Method 1: Using set\n",
        "print(\"Using set:\", len(set(lst)))\n",
        "\n",
        "# Method 2: Manual method\n",
        "unique = []\n",
        "for item in lst:\n",
        "    if item not in unique:\n",
        "        unique.append(item)\n",
        "print(\"Using manual loop:\", len(unique))\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "fed6677c",
      "metadata": {
        "id": "fed6677c"
      },
      "source": [
        "**31-write a python program Extract all elements with Frequency greater than K (Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3\n",
        "Output : [4, 3] )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d81f3f9d",
      "metadata": {
        "id": "d81f3f9d",
        "outputId": "ee320e1d-a794-4dfe-8fc1-7c1a9219e072",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[4, 3]\n"
          ]
        }
      ],
      "source": [
        "# Elements with frequency greater than K\n",
        "\n",
        "test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]\n",
        "K = 3\n",
        "freq = {}\n",
        "\n",
        "for item in test_list:\n",
        "    if item in freq:\n",
        "        freq[item] += 1\n",
        "    else:\n",
        "        freq[item] = 1\n",
        "\n",
        "result = []\n",
        "for key in freq:\n",
        "    if freq[key] > K:\n",
        "        result.append(key)\n",
        "\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "caca5224",
      "metadata": {
        "id": "caca5224"
      },
      "source": [
        "**32-write a python program to find the Strongest Neighbour (Input: 1 2 2 3 4 5\n",
        "Output: 2 2 3 4 5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "39fbd9b2",
      "metadata": {
        "id": "39fbd9b2",
        "outputId": "ca02fd88-ba10-4756-dfc7-e350b8e88f24",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 2 3 4 5 "
          ]
        }
      ],
      "source": [
        "# Strongest neighbour: max between adjacent elements\n",
        "\n",
        "arr = [1, 2, 2, 3, 4, 5]\n",
        "n = len(arr)\n",
        "\n",
        "for i in range(n - 1):\n",
        "    print(max(arr[i], arr[i + 1]), end=\" \")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "a9fa8baf",
      "metadata": {
        "id": "a9fa8baf"
      },
      "source": [
        "**33-write a Python Program to print all Possible Combinations from the three Digits (Input: [1, 2, 3]\n",
        "Output:\n",
        "1 2 3 ##\n",
        "1 3 2 ##\n",
        "2 1 3 ##\n",
        "2 3 1 ##\n",
        "3 1 2 ##\n",
        "3 2 1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8c520a76",
      "metadata": {
        "id": "8c520a76",
        "outputId": "235e9156-3e4a-4b87-d6ff-8385431c7496",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n",
            "1 3 2\n",
            "2 1 3\n",
            "2 3 1\n",
            "3 1 2\n",
            "3 2 1\n"
          ]
        }
      ],
      "source": [
        "# All possible combinations of 3 digits\n",
        "\n",
        "digits = [1, 2, 3]\n",
        "\n",
        "for i in digits:\n",
        "    for j in digits:\n",
        "        for k in digits:\n",
        "            if i != j and j != k and i != k:\n",
        "                print(i, j, k)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "5288bb89",
      "metadata": {
        "id": "5288bb89"
      },
      "source": [
        "**34-write a Python program to find all the Combinations in the list with the given condition (Input: test_list = [1,2,3]\n",
        "Output:\n",
        " [1], [1, 2], [1, 2, 3], [1, 3]\n",
        " [2], [2, 3], [3])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "59b89646",
      "metadata": {
        "id": "59b89646",
        "outputId": "a44583d3-a98d-4009-d547-3cc4c6577c3d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]\n"
          ]
        }
      ],
      "source": [
        "# All combinations (continuous or not)\n",
        "\n",
        "from itertools import combinations\n",
        "\n",
        "test_list = [1, 2, 3]\n",
        "all_combinations = []\n",
        "\n",
        "for r in range(1, len(test_list) + 1):\n",
        "    for combo in combinations(test_list, r):\n",
        "        all_combinations.append(list(combo))\n",
        "\n",
        "print(all_combinations)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "39973705",
      "metadata": {
        "id": "39973705"
      },
      "source": [
        "**35-write a Python program to get all unique combinations of two Lists (List_1 = [\"a\",\"b\"]\n",
        "List_2 = [1,2]\n",
        "Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8c4ba22b",
      "metadata": {
        "id": "8c4ba22b",
        "outputId": "ee462b58-1c28-4839-eb11-199e2423ff6d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[('a', 1), ('b', 2)], [('a', 2), ('b', 1)]]\n"
          ]
        }
      ],
      "source": [
        "# Unique combinations of two lists\n",
        "\n",
        "from itertools import permutations\n",
        "\n",
        "list_1 = [\"a\", \"b\"]\n",
        "list_2 = [1, 2]\n",
        "\n",
        "result = []\n",
        "\n",
        "for perm in permutations(list_2):\n",
        "    pair = [(list_1[i], perm[i]) for i in range(len(list_1))]\n",
        "    result.append(pair)\n",
        "\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "25199af5",
      "metadata": {
        "id": "25199af5"
      },
      "source": [
        "**36-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1\n",
        "\n",
        "**Output : 2 3 4 5 2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6dc4c2ba",
      "metadata": {
        "id": "6dc4c2ba",
        "outputId": "c14dd072-e7eb-4d21-e8ee-0c551c980a10",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 3, 4, 5, 2]\n"
          ]
        }
      ],
      "source": [
        "lst = [1, 1, 2, 3, 4, 5, 1, 2, 1]\n",
        "element_to_remove = 1\n",
        "result = [x for x in lst if x != element_to_remove]\n",
        "print(result)  # Output: [2, 3, 4, 5, 2]\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "bf1a3c93",
      "metadata": {
        "id": "bf1a3c93"
      },
      "source": [
        "**37-write a python program to Replace index elements with elements in Other List (The original list 1 is : [‘Gfg’, ‘is’, ‘best’] The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0] The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fdd66a71",
      "metadata": {
        "id": "fdd66a71",
        "outputId": "83e23b7e-4f13-421b-cf49-d639a3cffb6d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Gfg', 'is', 'best', 'is', 'Gfg', 'Gfg', 'Gfg', 'best', 'is', 'is', 'best', 'Gfg']\n"
          ]
        }
      ],
      "source": [
        "list1 = ['Gfg', 'is', 'best']\n",
        "list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]\n",
        "result = [list1[i] for i in list2]\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "af0f56e8",
      "metadata": {
        "id": "af0f56e8"
      },
      "source": [
        "**38- write python program to Retain records with N occurrences of K(Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2\n",
        "Output : [(4, 5, 5, 4)]\n",
        "Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3\n",
        "Output : [] )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "67b06671",
      "metadata": {
        "id": "67b06671",
        "outputId": "61522b13-7abe-4748-8d6e-323097392563",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(4, 5, 5, 4)]\n"
          ]
        }
      ],
      "source": [
        "test_list = [(4, 5, 5, 4), (5, 4, 3)]\n",
        "K = 5\n",
        "N = 2\n",
        "result = [tpl for tpl in test_list if tpl.count(K) == N]\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "de76f183",
      "metadata": {
        "id": "de76f183"
      },
      "source": [
        "**39-write a Python Program to Sort the list according to the column using lambda\n",
        "array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]\n",
        "Output :\n",
        "Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]]\n",
        "Sorted array specific to column 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]]\n",
        "Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "dc883308",
      "metadata": {
        "id": "dc883308",
        "outputId": "4b7a7b14-daa6-4bcb-a2ca-c393dee5f2fe",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sorted by column 0: [[1, 3, 3], [2, 1, 2], [3, 2, 1]]\n",
            "Sorted by column 1: [[2, 1, 2], [3, 2, 1], [1, 3, 3]]\n",
            "Sorted by column 2: [[3, 2, 1], [2, 1, 2], [1, 3, 3]]\n"
          ]
        }
      ],
      "source": [
        "array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]\n",
        "for i in range(3):\n",
        "    sorted_array = sorted(array, key=lambda x: x[i])\n",
        "    print(f\"Sorted by column {i}: {sorted_array}\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**40- write a program to Sort Python Dictionaries by Key or Value"
      ],
      "metadata": {
        "id": "lM-_6Uiy9c9F"
      },
      "id": "lM-_6Uiy9c9F"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d2e7b31f",
      "metadata": {
        "id": "d2e7b31f",
        "outputId": "8ac47ef9-9352-4c2b-c867-36cd47024871",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}\n"
          ]
        }
      ],
      "source": [
        "data = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}\n",
        "sorted_dict = dict(sorted(data.items()))\n",
        "print(sorted_dict)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "ec63c23a",
      "metadata": {
        "id": "ec63c23a"
      },
      "source": [
        "**41-write python program to Remove keys with Values Greater than K ( Including mixed values )\n",
        "nput : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’},\n",
        "K = 7\n",
        "Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e39c3a40",
      "metadata": {
        "id": "e39c3a40",
        "outputId": "4921696d-ebf8-45e8-c615-e76b43522889",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'Gfg': 3, 'is': 7, 'for': 6, 'geeks': 'CS'}\n"
          ]
        }
      ],
      "source": [
        "test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}\n",
        "K = 7\n",
        "result = {k: v for k, v in test_dict.items() if not (isinstance(v, int) and v > K)}\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f143f0fe",
      "metadata": {
        "id": "f143f0fe"
      },
      "source": [
        "**42-Write a Python program to concatenate the following dictionaries to create a new one\n",
        "\n",
        "Sample Dictionary :\n",
        "dic1={1:10, 2:20}\n",
        "dic2={3:30, 4:40}\n",
        "dic3={5:50,6:60}\n",
        "Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "74ffdfea",
      "metadata": {
        "id": "74ffdfea",
        "outputId": "1743a734-b8d4-49ad-926c-809116570113",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}\n"
          ]
        }
      ],
      "source": [
        "dic1 = {1: 10, 2: 20}\n",
        "dic2 = {3: 30, 4: 40}\n",
        "dic3 = {5: 50, 6: 60}\n",
        "result = {**dic1, **dic2, **dic3}\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "fb04c93c",
      "metadata": {
        "id": "fb04c93c"
      },
      "source": [
        "**43-Write a Python program to iterate over dictionaries using for loops"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6aebc470",
      "metadata": {
        "id": "6aebc470",
        "outputId": "8b56ad2c-755b-4085-f74e-9b0c586ca2ce",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "a: 1\n",
            "b: 2\n",
            "c: 3\n"
          ]
        }
      ],
      "source": [
        "my_dict = {'a': 1, 'b': 2, 'c': 3}\n",
        "for key, value in my_dict.items():\n",
        "    print(f\"{key}: {value}\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "5f491a9d",
      "metadata": {
        "id": "5f491a9d"
      },
      "source": [
        "**44- Write a Python script to merge two Python dictionaries"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b8a14028",
      "metadata": {
        "id": "b8a14028"
      },
      "outputs": [],
      "source": [
        "dict1 = {'a': 1, 'b': 2}\n",
        "dict2 = {'c': 3, 'd': 4}\n",
        "dict1.update(dict2)\n",
        "print(dict1)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "216fc72d",
      "metadata": {
        "id": "216fc72d"
      },
      "source": [
        "**45-Write a Python program to get the maximum and minimum values of a dictionary values"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d6883f5f",
      "metadata": {
        "id": "d6883f5f",
        "outputId": "a512a206-75de-4d01-e90e-5e6bacfeb5b6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Max: 30\n",
            "Min: 5\n"
          ]
        }
      ],
      "source": [
        "data = {'a': 10, 'b': 5, 'c': 30}\n",
        "print(\"Max:\", max(data.values()))\n",
        "print(\"Min:\", min(data.values()))\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b6a53011",
      "metadata": {
        "id": "b6a53011"
      },
      "source": [
        "**46- Write a Python program to drop empty items from a given dictionary.\n",
        "Original Dictionary:\n",
        "{'c1': 'Red', 'c2': 'Green', 'c3': None}\n",
        "New Dictionary after dropping empty items:\n",
        "{'c1': 'Red', 'c2': 'Green'}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b5c6fecf",
      "metadata": {
        "id": "b5c6fecf",
        "outputId": "ecd81186-942f-468a-b7df-2499d8e1af61",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'c1': 'Red', 'c2': 'Green'}\n"
          ]
        }
      ],
      "source": [
        "original = {'c1': 'Red', 'c2': 'Green', 'c3': None}\n",
        "cleaned = {k: v for k, v in original.items() if v is not None}\n",
        "print(cleaned)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "46d718c7",
      "metadata": {
        "id": "46d718c7"
      },
      "source": [
        "**47-Write a Python program to create a tuple of numbers and print one item"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "13216ff5",
      "metadata": {
        "id": "13216ff5",
        "outputId": "1e4ea1b3-d77e-472c-b3ac-5948dbd4e957",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ],
      "source": [
        "t = (1, 2, 3, 4)\n",
        "print(t[2])  # prints 3\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "2be5b56b",
      "metadata": {
        "id": "2be5b56b"
      },
      "source": [
        "**48-Write a Python program to unpack a tuple into several variables"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "595f44be",
      "metadata": {
        "id": "595f44be",
        "outputId": "62969f24-ca88-44f2-fbc0-bf4ac25cb620",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n"
          ]
        }
      ],
      "source": [
        "t = (1, 2, 3)\n",
        "a, b, c = t\n",
        "print(a, b, c)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "392388a7",
      "metadata": {
        "id": "392388a7"
      },
      "source": [
        "**49-Write a Python program to add an item to a tuple"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "54cc092e",
      "metadata": {
        "id": "54cc092e",
        "outputId": "790795d0-7764-4a19-c7d7-bd27a7ffbb7a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 2, 3, 4)\n"
          ]
        }
      ],
      "source": [
        "t = (1, 2, 3)\n",
        "t = t + (4,)\n",
        "print(t)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3e8fd124",
      "metadata": {
        "id": "3e8fd124"
      },
      "source": [
        "**50-Write a Python program to convert a tuple to a string"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "92a71ddc",
      "metadata": {
        "id": "92a71ddc",
        "outputId": "b3d10be4-7495-4511-ffc9-3ee69f6b67da",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "abc\n"
          ]
        }
      ],
      "source": [
        "t = ('a', 'b', 'c')\n",
        "s = ''.join(t)\n",
        "print(s)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f4f64ef4",
      "metadata": {
        "id": "f4f64ef4"
      },
      "source": [
        "**51-Write a Python program to convert a list to a tuple"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "210d56d3",
      "metadata": {
        "id": "210d56d3",
        "outputId": "46a56927-e46e-4207-a20e-d28ef068a0d0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 2, 3)\n"
          ]
        }
      ],
      "source": [
        "lst = [1, 2, 3]\n",
        "t = tuple(lst)\n",
        "print(t)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b1e00ef7",
      "metadata": {
        "id": "b1e00ef7"
      },
      "source": [
        "**52-Write a Python program to reverse a tuple"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f45bfdc7",
      "metadata": {
        "id": "f45bfdc7",
        "outputId": "2787e303-47ed-466b-cb73-fde38cd14a07",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(3, 2, 1)\n"
          ]
        }
      ],
      "source": [
        "t = (1, 2, 3)\n",
        "reversed_t = t[::-1]\n",
        "print(reversed_t)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3cd347d1",
      "metadata": {
        "id": "3cd347d1"
      },
      "source": [
        "**53-Write a Python program to replace the last value of tuples in a list.\n",
        "Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]\n",
        "Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3c4a2a4c",
      "metadata": {
        "id": "3c4a2a4c",
        "outputId": "c94353b8-646c-40c3-e607-b3e287fefe34",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(10, 20, 100), (40, 50, 100), (70, 80, 100)]\n"
          ]
        }
      ],
      "source": [
        "lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]\n",
        "result = [tpl[:-1] + (100,) for tpl in lst]\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "76bb7b39",
      "metadata": {
        "id": "76bb7b39"
      },
      "source": [
        "**54-Write a Python program to convert a given string list to a tuple\n",
        "Original string: python 3.0\n",
        "<class 'str'>\n",
        "Convert the said string to a tuple:\n",
        "('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "51951937",
      "metadata": {
        "id": "51951937",
        "outputId": "556585e6-36f1-482c-db53-f299c7c3ce4c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')\n"
          ]
        }
      ],
      "source": [
        "s = \"python3.0\"\n",
        "t = tuple(s)\n",
        "print(t)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "5a1d5d97",
      "metadata": {
        "id": "5a1d5d97"
      },
      "source": [
        "**55-Write a Python program to calculate the average value of the numbers in a given tuple of tuples"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "834e7992",
      "metadata": {
        "id": "834e7992"
      },
      "outputs": [],
      "source": [
        "tups = ((1, 2), (3, 4), (5, 6))\n",
        "flattened = [item for sub in tups for item in sub]\n",
        "average = sum(flattened) / len(flattened)\n",
        "print(average)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "51edab9c",
      "metadata": {
        "id": "51edab9c"
      },
      "source": [
        "**56-Write a Python program to add member(s) to a set."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "2b65df79",
      "metadata": {
        "id": "2b65df79",
        "outputId": "6976b8cf-f134-4ce0-9343-9b2f91e40558",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1, 2, 3, 4, 5}\n"
          ]
        }
      ],
      "source": [
        "s = {1, 2}\n",
        "s.add(3)\n",
        "s.update([4, 5])\n",
        "print(s)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "965590cc",
      "metadata": {
        "id": "965590cc"
      },
      "source": [
        "**57-Write a Python program to remove an item from a set if it is present in the set."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "866bab28",
      "metadata": {
        "id": "866bab28",
        "outputId": "73c6f2a1-822f-412c-94f8-4da012197ecc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1, 3}\n"
          ]
        }
      ],
      "source": [
        "s = {1, 2, 3}\n",
        "s.discard(2)  # Won't raise error if not found\n",
        "print(s)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "2b7cfed1",
      "metadata": {
        "id": "2b7cfed1"
      },
      "source": [
        "**58-Write a Python program to create an intersection,union,difference and symmetric difference of sets"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7f94b7fe",
      "metadata": {
        "id": "7f94b7fe",
        "outputId": "33afae93-ca32-4651-9664-6cdf5fb49267",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intersection: {3}\n",
            "Union: {1, 2, 3, 4, 5}\n",
            "Difference: {1, 2}\n",
            "Symmetric Difference: {1, 2, 4, 5}\n"
          ]
        }
      ],
      "source": [
        "a = {1, 2, 3}\n",
        "b = {3, 4, 5}\n",
        "print(\"Intersection:\", a & b)\n",
        "print(\"Union:\", a | b)\n",
        "print(\"Difference:\", a - b)\n",
        "print(\"Symmetric Difference:\", a ^ b)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b94931e2",
      "metadata": {
        "id": "b94931e2"
      },
      "source": [
        "**59-Write a Python program to find the maximum and minimum values in a set"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "203f9600",
      "metadata": {
        "id": "203f9600",
        "outputId": "b5507c65-0ed3-493a-a1c0-70738d1dc38e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Max: 9\n",
            "Min: 1\n"
          ]
        }
      ],
      "source": [
        "s = {4, 7, 1, 9}\n",
        "print(\"Max:\", max(s))\n",
        "print(\"Min:\", min(s))\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "255fd554",
      "metadata": {
        "id": "255fd554"
      },
      "source": [
        "**60- Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c2d94e1f",
      "metadata": {
        "id": "c2d94e1f",
        "outputId": "220d05d0-ca41-4ea7-d8c2-a854e8dd46cd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(1, 5), (1, 5), (7, -1)]\n"
          ]
        }
      ],
      "source": [
        "lst = [1, 5, 7, -1, 5]\n",
        "target = 6\n",
        "result = []\n",
        "for i in range(len(lst)):\n",
        "    for j in range(i+1, len(lst)):\n",
        "        if lst[i] + lst[j] == target:\n",
        "            result.append((lst[i], lst[j]))\n",
        "print(result)\n"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
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
      "version": "3.9.7"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}