﻿/*
Deployment script for TestDB

This code was generated by a tool.
Changes to this file may cause incorrect behavior and will be lost if
the code is regenerated.
*/

GO
SET ANSI_NULLS, ANSI_PADDING, ANSI_WARNINGS, ARITHABORT, CONCAT_NULL_YIELDS_NULL, QUOTED_IDENTIFIER ON;

SET NUMERIC_ROUNDABORT OFF;


GO
:setvar DatabaseName "TestDB"
:setvar DefaultFilePrefix "TestDB"
:setvar DefaultDataPath "C:\Users\e.kolpakov\AppData\Local\Microsoft\Microsoft SQL Server Local DB\Instances\MSSQLLocalDB\"
:setvar DefaultLogPath "C:\Users\e.kolpakov\AppData\Local\Microsoft\Microsoft SQL Server Local DB\Instances\MSSQLLocalDB\"

GO
:on error exit
GO
/*
Detect SQLCMD mode and disable script execution if SQLCMD mode is not supported.
To re-enable the script after enabling SQLCMD mode, execute the following:
SET NOEXEC OFF; 
*/
:setvar __IsSqlCmdEnabled "True"
GO
IF N'$(__IsSqlCmdEnabled)' NOT LIKE N'True'
    BEGIN
        PRINT N'SQLCMD mode must be enabled to successfully execute this script.';
        SET NOEXEC ON;
    END


GO
USE [$(DatabaseName)];


GO
PRINT N'Creating View [dbo].[FullInfo]...';


GO
CREATE VIEW [dbo].[FullInfo]
	AS 
	SELECT [p].[PersonId], [p].[FirstName], [p].[LastName], [i].[Email], [i].[NumerOfPets]
	FROM dbo.PersonalData p
	LEFT JOIN dbo.AdditionalInfo a ON p.PersonId = a.PersonId
	LEFT JOIN dbo.AdditionalInfo i on i.PersonId = p.PersonId;
GO
/*
Post-Deployment Script Template							
--------------------------------------------------------------------------------------
 This file contains SQL statements that will be appended to the build script.		
 Use SQLCMD syntax to include a file in the post-deployment script.			
 Example:      :r .\myfile.sql								
 Use SQLCMD syntax to reference a variable in the post-deployment script.		
 Example:      :setvar TableName MyTable							
               SELECT * FROM [$(TableName)]					
--------------------------------------------------------------------------------------
*/
IF not exists (SELECT * FROM dbo.PersonalData WHERE FirstName = 'Charles' and LastName = 'Brown')
BEGIN
    INSERT INTO dbo.PersonalData (FirstName, LastName)
    VALUES('Charles', 'Brown');
END 
GO

GO
PRINT N'Update complete.';


GO
