using Microsoft.Extensions.DependencyInjection;

public static class DIFactory
{
    public static IServiceCollection AddAllDependencies(this IServiceCollection services)
    {
        services
                .AddScoped<IGreetingHandler,BlobGreetingHandler>()
                .AddScoped<IMessageFormatter,DateMessageFormatter>()

        ;

        return services;
    }
}