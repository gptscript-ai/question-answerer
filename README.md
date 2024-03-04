# Question-Answerer

Question-Answerer is a wrapper around the [GPTScript search tools](https://github.com/gptscript-ai/search). It allows you to ask questions and get answers from the web, and it cites its sources.

Example:

```bash
gptscript --sub-tool=question-answerer-ddg --cache=false tool.gpt --question="Who were the first people to climb Mount Everest?"
```

Response:

```
- [ThoughtCo](https://www.thoughtco.com/the-first-to-climb-mount-everest-1779350)
- [Wikipedia](https://en.wikipedia.org/wiki/Edmund_Hillary)
- [National Geographic](https://www.nationalgeographic.com/adventure/article/sir-edmund-hillary-tenzing-norgay-1953)
- [History Hit](https://www.historyhit.com/was-george-mallory-actually-the-first-man-to-climb-everest/)

The first people to climb Mount Everest were New Zealander Edmund Hillary and Nepalese Sherpa Tenzing Norgay. They reached the summit at 11:30 a.m. on May 29, 1953, as part of the ninth British expedition to Everest, led by John Hunt. Their achievement was a significant moment in mountaineering history and made them international celebrities. The expedition was meticulously planned and executed, with a large team supporting the climbers. Before Hillary and Norgay's successful ascent, Everest had repulsed many expeditions. The 1953 expedition was notable for its military-style organization and the use of oxygen, which was controversial at the time. Hillary and Norgay's success came after a failed attempt by Tom Bourdillon and Charles Evans, who reached the South Summit but turned back due to exhaustion and oxygen problems.

There has been speculation about whether George Mallory and Andrew Irvine might have reached the summit before Hillary and Norgay during their 1924 expedition. Mallory's body was found in 1999, but Irvine's remains and the camera they carried have never been discovered. Some believe that if the camera were found, it might provide evidence of whether they reached the summit. However, the route they took was extremely challenging, and while it's possible they might have reached the summit, it is considered unlikely by many.
```

## Setup and Usage

```bash
# Clone the search tools repo
git clone https://github.com/gptscript-ai/search.git

# Build it
(cd search && make build)

# Clone this repo
git clone https://github.com/gptscript-ai/question-answerer.git

# Set up the venv
cd question-answerer
python3 -m venv .venv

# Source it
source .venv/bin/activate

# Install the packages
pip3 install -r requirements.txt

# Run the tool
gptscript --sub-tool="question-answerer-ddg" --cache=false tool.gpt --question="Who were the first people to climb Mount Everest?"
```
