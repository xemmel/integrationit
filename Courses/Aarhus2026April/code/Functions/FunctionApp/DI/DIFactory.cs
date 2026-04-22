using Microsoft.Extensions.DependencyInjection;

public static class DIFactory
{
    public static IServiceCollection AddCompanyServices(this IServiceCollection services)
    {
        services
           .AddScoped<IOrderHandler,SpecialSaleOrderHandler>();

        return services;
    }
}