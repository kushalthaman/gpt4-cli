<img width="907" alt="Screenshot 2023-11-22 at 1 10 56 AM" src="https://github.com/kushalthaman/gpt4-cli/assets/62183606/80f1369f-a186-44ad-be4f-39458b3dc2e3">


> notes:
- you'll need to use your own api key for running the files
- I've spent an hour building this, so it only has basic functionality. For future work here, I may add text-stream, make this into a web terminal hosted on a server, add multi-turn dialogue functionality, integrate plugins/external api's, etc.

features:
>cli.py:
- takes in system prompt, and outputs a single bash command
- has an oversight mechanism: cannot run arbitrary commands without oversight (asking for approval before running it)
- prints the result of the output command, and resets to 'query>' once done
- see example in attached file above

>cli-stream.py
- cli.py streams output tokens one by one
- currently the functionality here needs to be slightly fixed to not have <bash> </bash> and query> at the end of outputs


