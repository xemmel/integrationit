```csharp

using Microsoft.BizTalk.ExplorerOM;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace BizTalkFilterExtract
{
    class Program
    {

        static string TranslateFilter(string filterXml)
        {
            if (string.IsNullOrWhiteSpace(filterXml))
            {
                return null;
            }
            // Load the XML document
            XDocument xmlDoc = XDocument.Parse(filterXml);

            // StringBuilder for constructing the boolean expression
            StringBuilder expression = new StringBuilder();

            // Iterate through all "Group" elements
            foreach (var group in xmlDoc.Descendants("Group"))
            {
                foreach (var statement in group.Descendants("Statement"))
                {
                    // Extract attributes
                    string property = statement.Attribute("Property")?.Value;
                    string op = GetOperator(statement.Attribute("Operator")?.Value);
                    string value = statement.Attribute("Value")?.Value;

                    // Append the statement
                    if (expression.Length > 0)
                    {
                        expression.Append(" OR "); // Use OR to combine groups
                    }
                    expression.Append($"{property} {op} '{value}'");
                }
            }

            return expression.ToString();
        }

        static string GetOperator(string operatorValue)
        {
            // Map BizTalk operator codes to human-readable operators
            switch (operatorValue)
            {
                case "0": return "=";
                case "1": return "!=";
                case "2": return "<";
                case "3": return "<=";
                case "4": return ">";
                case "5": return ">=";
                case "6": return "EXISTS";
                case "7": return "NOT EXISTS";
                default: return "UNKNOWN";
            }
        }


        static void Main(string[] args)
        {
            string mgmtDbServer = "biztalkdev";
            string mgmtDbName = "BizTalkMgmtDb";

            BtsCatalogExplorer explorer = new BtsCatalogExplorer
            {
                ConnectionString = $"Server={mgmtDbServer};Database={mgmtDbName};Integrated Security=SSPI;"
            };

            // Iterate through Send Ports and Output Filter Details
            List<SendPortModel> sendPorts = new List<SendPortModel>();
            foreach (SendPort sendPort in explorer.SendPorts)
            {
                if (sendPort.SendPipelineData == null)
                    continue;
                SendPortModel sendPortModel = new SendPortModel()
                {
                    Application = sendPort.Application.Name,
                    Name = sendPort.Name,
                    XmlFilter = sendPort.Filter,
                    Filter = TranslateFilter(sendPort.Filter),
                    PipelineConfig = sendPort.SendPipelineData


                };
                sendPorts.Add(sendPortModel);
           
            }
            var theSendPorts = sendPorts;

            var groupedData = sendPorts
           .GroupBy(sp => sp.Application)
           .ToDictionary(g => g.Key, g => g.ToList());

            string json = JsonConvert.SerializeObject(groupedData, Formatting.Indented);

            // Output JSON
            Console.WriteLine(json);



        }
    }
}


```