using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using System.Net.WebSockets;
using System.Threading;
using WebSocketServer.Middleware;

namespace WebSocketServer
{
    public class Startup
    {

        public void ConfigureServices(IServiceCollection services)
        {
        }

        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            app.UseWebSockets();

            app.Run(async context =>
            {
                Console.WriteLine("Hello from 3rd (terminal) Request Delegate");
                await context.Response.WriteAsync("Hello from 3rd (terminal) Request Delegate");
            });
        } 
    }
}