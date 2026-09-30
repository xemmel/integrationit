```powershell

cd c:\code\integrationit
git reset --hard HEAD
git pull

cd c:\code\integrationit\AI\AI103\students\agents


python .\create_agent.py --name tools-[init]-agent --deployment mini --instructions "You are a non-wise chat bot"

python app_agent_tools.py --agent tools-[init]-agent

```