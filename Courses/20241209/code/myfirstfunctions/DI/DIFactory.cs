using Microsoft.Extensions.DependencyInjection;

public static class DIFactory
{
    public static IServiceCollection AddAllDependenciesForMyFirstFunctions(this IServiceCollection services)
    {
        services
            .AddScoped<IGreetHandler,AngryGreeter>()
            .AddScoped<IStringFormatter, DateStringFormatter>()
            ;
        return services;
    }
}