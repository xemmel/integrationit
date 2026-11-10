```powershell

python .\agent.py --agent_name agent2 --model large --customtools --instructions "You are a chat bot, only answer in XML"

python .\chat.py --agent agent2



## RAG

python .\vectorstore.py --name "emp-vector-store2"

python .\agent.py --agent_name agent4 --model large --customtools --instructions "You are a chat bot. You have access to employee data via. RAG" --vector_store_id vs_vpDxbtaMBpusj1kmC5bNm1YY



```