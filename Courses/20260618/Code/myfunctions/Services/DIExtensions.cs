using Microsoft.Extensions.DependencyInjection;

public static class DIExtensions
{
    public static IServiceCollection AddAllMyServices(this IServiceCollection services)
    {
        services
           .AddScoped<IProcessOrderService,ProcessChristOrderService>()
           ;
        return services;
    }
}