public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();
    services.AddDbContext<ApplicationDbContext>(options =>
        options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));
    services.AddScoped<MetaTraderService>();
}
