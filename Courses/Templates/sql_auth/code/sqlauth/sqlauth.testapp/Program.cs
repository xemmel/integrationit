using System.Data;
using System.Text;
using Dapper;
using Microsoft.Data.SqlClient;


StringBuilder connectionString = new StringBuilder();
connectionString.Append(@"Server=tcp:mlcserver.database.windows.net,1433;");
connectionString.Append(@"Database=mlcdatabase;");
connectionString.Append(@"Authentication=Active Directory Default;");
connectionString.Append(@"Encrypt=True;");


var con = new SqlConnection(connectionString.ToString());
await con.OpenAsync();
System.Console.WriteLine("Connection opened...");


if ((args.Length > 0) && (args[0].ToLower().Equals("write")))
{
    string title = args[1];
    string sql = "INSERT INTO dbo.Songs (Title) VALUES (@Title)";
    await con.ExecuteAsync(sql, new { Title = title });
    System.Console.WriteLine("inserted..");
}
else if((args.Length > 0) && (args[0].ToLower().Equals("delete")))
{
    int songId = int.Parse(args[1]);
    string sql = "DELETE FROM dbo.Songs where SongId = @Id";
    await con.ExecuteAsync(sql, new { Id = songId });
    System.Console.WriteLine("deleted..");
}
else
{
    string sql = "select * from dbo.Songs";
    var result = await con.QueryAsync<dynamic>(sql);
    foreach (var item in result)
    {
        System.Console.WriteLine($"{item.SongId}\t{item.Title}");
    }
}
