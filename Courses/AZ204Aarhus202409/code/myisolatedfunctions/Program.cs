using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var host = new HostBuilder()
    .ConfigureServices(s => s
        .AddAllDependencies()
    )
    .ConfigureFunctionsWorkerDefaults()
    .Build();

host.Run();
