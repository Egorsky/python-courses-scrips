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
PRINT N'Rename refactoring operation with key 737a6933-befb-42d3-ae1d-d74593226da2 is skipped, element [dbo].[AdditionalInfo].[Id] (SqlSimpleColumn) will not be renamed to PersonId';


GO
PRINT N'Creating Table [dbo].[AdditionalInfo]...';


GO
CREATE TABLE [dbo].[AdditionalInfo] (
    [PersonId]    INT          NOT NULL,
    [Email]       VARCHAR (50) NULL,
    [NumerOfPets] NCHAR (10)   NULL,
    PRIMARY KEY CLUSTERED ([PersonId] ASC)
);


GO
PRINT N'Creating Foreign Key [dbo].[FK_AdditionalInfo_ToTable]...';


GO
ALTER TABLE [dbo].[AdditionalInfo] WITH NOCHECK
    ADD CONSTRAINT [FK_AdditionalInfo_ToTable] FOREIGN KEY ([PersonId]) REFERENCES [dbo].[PersonalData] ([PersonId]);


GO
-- Refactoring step to update target server with deployed transaction logs
IF NOT EXISTS (SELECT OperationKey FROM [dbo].[__RefactorLog] WHERE OperationKey = '737a6933-befb-42d3-ae1d-d74593226da2')
INSERT INTO [dbo].[__RefactorLog] (OperationKey) values ('737a6933-befb-42d3-ae1d-d74593226da2')

GO

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
PRINT N'Checking existing data against newly created constraints';


GO
USE [$(DatabaseName)];


GO
ALTER TABLE [dbo].[AdditionalInfo] WITH CHECK CHECK CONSTRAINT [FK_AdditionalInfo_ToTable];


GO
PRINT N'Update complete.';


GO
